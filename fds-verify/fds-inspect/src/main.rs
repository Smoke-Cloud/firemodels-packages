use clap::{Arg, Command, value_parser};
use std::path::PathBuf;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // env_logger::init();
    let matches = Command::new("fds-inspect")
        .arg_required_else_help(true)
        .version(clap::crate_version!())
        .author("Jake O'Shannessy <joshannessy@smokecloud.io>")
        .about("FDS Inspect CLI")
        .arg(
            Arg::new("INPUT-PATH")
                .required(true)
                .num_args(1)
                .help("Path to the input file or '-' for stdin"),
        )
        .arg(
            Arg::new("FDS-VERSION")
                .value_parser(value_parser!(semver::Version))
                .long("fds-version")
                .required(false)
                .num_args(1)
                .help("The version of FDS to use"),
        )
        .arg(
            Arg::new("OUT-PARAM")
                .num_args(1)
                .help("The version of FDS to use"),
        )
        .get_matches();

    let fds_input_path = matches
        .get_one::<String>("INPUT-PATH")
        .expect("No input path");

    let fds_verify_path: PathBuf = {
        let t: PathBuf = std::env::var("FDS_VERIFY_PATH")
            .unwrap()
            .parse::<PathBuf>()
            .unwrap();
        PathBuf::from(t.parent().unwrap())
    };

    let fds_version = matches
        .get_one::<semver::Version>("FDS-VERSION")
        .cloned()
        .unwrap_or_else(|| "6.10.1".parse().unwrap());

    let mut p = fds_verify_path.join(format!("fds-verify-{}", fds_version));
    p.add_extension(std::env::consts::EXE_EXTENSION);

    let def = "-".to_string();
    let out_param = matches.get_one::<String>("OUT-PARAM").unwrap_or(&def);
    std::process::Command::new(p)
        .arg(fds_input_path)
        .arg("--json")
        .arg(out_param)
        .spawn()
        .expect("failed to start")
        .wait()
        .unwrap();

    Ok(())
}
