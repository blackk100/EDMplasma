mkdir -p ~/projects

python3 -m venv .venv
. ~/projects/.venv/bin/activate
pip install -r requirements.txt

git clone git@github.com:idaholab/moose.git
git clone git@github.com:arfc/squirrel.git
git clone git@github.com:lcpp-org/crane.git
git clone git@github.com:shannon-lab/zapdos.git
export CC=mpicc CXX=mpicxx FC=mpif90 F90=mpif90 F77=mpif77
export MOOSE_JOBS=16 METHODS=opt

cd moose
git checkout master
cd scripts
./update_and_rebuild_petsc.sh --download-bison --CC=$CC --CXX=$CXX --FC=$FC 2>&1 | tee petsc.log | grep -i --color=always -E "warning|error"
cd ~/projects/moose/petsc
make PETSC_DIR=~/projects/moose/petsc PETSC_ARCH=arch-moose check 2>&1 | tee check.log
cd ~/projects/moose/scripts
./update_and_rebuild_libmesh.sh 2>&1 | tee libmesh.log | grep -i --color=always -E "warning|error"
./update_and_rebuild_wasp.sh 2>&1 | tee wasp.log | grep -i --color=always -E "warning|error"
cd ~/projects/moose/test
make -j 4 2>&1 | tee build.log | grep -i --color=always -E "warning|error"
./run_tests -j 8 2>&1 | tee tests.log

cd ~/projects/squirrel
git checkout master
make -j 16 2>&1 | tee build.log | grep -i --color=always -E "warning|error"
./run_tests -j 8 2>&1 | tee tests.log

cd ~/projects/crane
git checkout master
rm -r moose
ln -s ~/projects/moose/ ./moose
make -j 16 2>&1 | tee build.log | grep -i --color=always -E "warning|error"
./run_tests -j 8 2>&1 | tee tests.log

cd ~/projects/zapdos
git checkout master
rm -r moose
rm -r squirrel
rm -r crane
ln -s ~/projects/moose/ ./moose
ln -s ~/projects/squirrel/ ./squirrel
ln -s ~/projects/crane/ ./crane
make -j 16 2>&1 | tee build.log | grep -i --color=always -E "warning|error"
./run_tests -j 8 2>&1 | tee tests.log
