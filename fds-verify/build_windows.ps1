# cmd.exe "/K" '"C:\Program Files (x86)\Intel\oneAPI\setvars.bat" && powershell'

$P = Import-Csv -Path .\versions.csv
$ProgressPreference = 'SilentlyContinue'
foreach ($row in $P) {
    if ($row.build -eq "1") {
        Write-Host "Building $($row.version)"
    } else {
        Write-Host "Skipping $($row.version)"
        continue
    }
    $dir = "windows_build/$($row.version)"
    mkdir -Force $dir
    $srcDir = "windows_build/$($row.version)/src"
    if (Test-Path $srcDir) { Remove-Item $srcDir -Recurse -Force }
    git clone --revision=$($row.commit) --depth 1 https://github.com/firemodels/$($row.repo).git $srcDir
    pushd $srcDir

    Write-Host "Applying " ../../../fds-$($row.version).patch
    git apply --allow-empty ../../../fds-$($row.version).patch
    if ($LastExitCode) {
        popd
        exit
    }
    # Write-Host "Applying " ../../../fds-$($row.version)-json.patch
    # git apply ../../../fds-$($row.version)-json.patch
    # if ($LastExitCode) {
    #     popd
    #     exit
    # }
    # Write-Host "Applying " ../../../json.patch
    # git apply ../../../json.patch
    # if ($LastExitCode) {
    #     popd
    #     exit
    # }
    cmd.exe "/C" '"C:\Program Files (x86)\Intel\oneAPI\setvars.bat" && cmake -B cbuild -DCMAKE_BUILD_TYPE=Release -DCMAKE_Fortran_COMPILER=ifx -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icx -GNinja -DUSE_HYPRE=OFF -DUSE_SUNDIALS=OFF -DUSE_OPENMP=OFF -DDUMP_JSON=ON'
    if ($LastExitCode) {
        popd
        exit
    }
    cmake --build cbuild -v -j6 --config Release
    if ($LastExitCode) {
        popd
        exit
    }
    cmake --install cbuild --prefix dist --config Release
    if ($LastExitCode) {
        popd
        exit
    }
    ctest --test-dir cbuild
    if ($LastExitCode) {
        popd
        exit
    }
    popd
}

# wix build .\FdsVerifyInstaller.wxs -out FdsVerifyInstaller_unsigned.msi
