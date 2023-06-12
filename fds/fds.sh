PROGRAM_NAME=fds
# The default number of MPI processes is 1
N_PROCESSES=1
TEMP=$(getopt --name $PROGRAM_NAME --options hvn: --longoptions help,version,intelmpi,openmpi,mkl -- "$@")

if [ $? -ne 0 ]; then
        echo "Error parsing arguments. Try $PROGRAM_NAME --help"
        exit
fi

usage() {
    printf "usage: fds [--version] [--help] <FDS-FILE>\n\n"
    printf "options:\n"
    printf "    -h/--help     Show this information.\n"
    printf "    -v/--version  Show version.\n"
    printf "    --intelmpi    Use Intel MPI.\n"
    printf "    --openmpi     Use Open MPI.\n"
    printf "    --mkl         Use MKL.\n"
    printf "    -n  Set the number of MPI processes.\n"
}

eval set -- "$TEMP"
while true; do
        case $1 in
                -h|--help)
                        usage
                        exit 0
                ;;
                -v|--version)
                        printf "%s %s\n" "$PROGRAM_NAME" "$FDS_VERSION"
                        exit 0
                ;;
                -n)
                        N_PROCESSES="$2"; shift 2; continue
                ;;
                --intelmpi)
                        USE_INTELMPI=true; shift 1; continue
                ;;
                --openmpi)
                        USE_OPENMPI=true; shift 1; continue
                ;;
                --mkl)
                        USE_MKL=true; shift 1; continue
                ;;
                --)
                        # End of options
                        break
                ;;
                *)
                        printf "Unknown option %s\n" "$1"
                        exit 1
                ;;
        esac
done
set "$@"
FDS_EXEC=$PROGRAM_NAME$FDS_VERSION
if [ "$USE_OPENMPI" = true ]; then
        if [ "$USE_INTELMPI" = true ]; then
                echo "Cannot specify Intel MPI and Open MPI simultaneously."
                exit 2
        fi
        if [ "$USE_MKL" = true ]; then
                echo "Cannot specify MKL and Open MPI simultaneously."
                exit 2
        fi
        module load mpi
else
        # Use Intel MPI by default. First we have to load the module files from
        # the OneAPI installations as they aren't loaded by default.
        module use /opt/intel/oneapi/modulefiles
        # Load mpi, this will now load intel mpi first
        module load mpi
        # Unlike openmpi, the intel modules don't set MPI_SUFFIX so we need to
        # do it here.
        MPI_SUFFIX=_intelmpi
        # The intel modules also don't account for the install location of
        # binaries so we add that to the path here.
        PATH="$PATH":/usr/lib64/intelmpi/bin
        if [ "$USE_MKL" = true ]; then
                module load mkl
                FDS_EXEC=$FDS_EXEC-mkl
        fi
fi
export I_MPI_COMPATIBILITY
if [ "$FDS_VERSION" = "5.5.3" ]; then
        # FDS 5 needs some MPI compatability options
        I_MPI_COMPATIBILITY=4
fi
exec mpiexec -np "$N_PROCESSES" "$FDS_EXEC"$MPI_SUFFIX "$@"
