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
                        printf "%s %s\n" "$PROGRAM_NAME" "$PROGRAM_VERSION"
                        exit 0
                ;;
                -n)
                        N_PROCESSES="$2"; shift 2; continue
                ;;
                --intelmpi)
                        USE_INTELMPI=true; shift 2; continue
                ;;
                --openmpi)
                        USE_OPENMPI=true; shift 2; continue
                ;;
                --mkl)
                        USE_MKL=true; shift 2; continue
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
FDS_EXEC=$PROGRAM_NAME
if [ "$USE_INTELMPI" = true ]; then
        if [ "$USE_OPENMPI" = true ]; then
                echo "Cannot specify Intel MPI and Open MPI simultaneously."
                exit 2
        fi
        module use /opt/intel/oneapi/modulefiles
        module load mpi
        FDS_EXEC=$FDS_EXEC-intelmpi
fi
if [ "$USE_OPENMPI" = true ]; then
        if [ "$USE_MKL" = true ]; then
                echo "Cannot specify MKL and Open MPI simultaneously."
                exit 2
        fi
        module load mpi
        FDS_EXEC=$FDS_EXEC-openmpi
fi
if [ "$USE_MKL" = true ]; then
        module use /opt/intel/oneapi/modulefiles
        module load mkl
        FDS_EXEC=$FDS_EXEC-mkl
fi
exec mpiexec -np "$N_PROCESSES" "$FDS_EXEC""$VERSION_SUFFIX" "$@"
