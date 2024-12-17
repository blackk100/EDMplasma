sed -i '/initial_condition = 7354.7/c\initial_condition = 5325.7' h2o.i
sed -i '/initial_condition = 2.366889807e17/c\initial_condition = 2.057936365e17' h2o.i
sed -i '/initial_condition = 1.577926538e20/c\initial_condition = 1.371957576e20' h2o.i
../../projects/crane/crane-opt -i h2o.i > run01.log 2>&1
mv h2o_out.csv h2o_out01.csv

sed -i '/initial_condition = 5325.7/c\initial_condition = 6171.1' h2o.i
../../projects/crane/crane-opt -i h2o.i > run02.log 2>&1
mv h2o_out.csv h2o_out02.csv

sed -i '/initial_condition = 6171.1/c\initial_condition = 6184.7' h2o.i
../../projects/crane/crane-opt -i h2o.i > run03.log 2>&1
mv h2o_out.csv h2o_out03.csv

sed -i '/initial_condition = 6184.7/c\initial_condition = 6691.5' h2o.i
../../projects/crane/crane-opt -i h2o.i > run04.log 2>&1
mv h2o_out.csv h2o_out04.csv

sed -i '/initial_condition = 6691.5/c\initial_condition = 6789.0' h2o.i
../../projects/crane/crane-opt -i h2o.i > run05.log 2>&1
mv h2o_out.csv h2o_out05.csv

sed -i '/initial_condition = 6789.0/c\initial_condition = 7181.5' h2o.i
../../projects/crane/crane-opt -i h2o.i > run06.log 2>&1
mv h2o_out.csv h2o_out06.csv

sed -i '/initial_condition = 7181.5/c\initial_condition = 5602.5' h2o.i
sed -i '/initial_condition = 2.057936365e17/c\initial_condition = 2.366889807e17' h2o.i
sed -i '/initial_condition = 1.371957576e20/c\initial_condition = 1.577926538e20' h2o.i
../../projects/crane/crane-opt -i h2o.i > run11.log 2>&1
mv h2o_out.csv h2o_out11.csv

sed -i '/initial_condition = 5602.5/c\initial_condition = 6446.5' h2o.i
../../projects/crane/crane-opt -i h2o.i > run12.log 2>&1
mv h2o_out.csv h2o_out12.csv

sed -i '/initial_condition = 6446.5/c\initial_condition = 6576.8' h2o.i
../../projects/crane/crane-opt -i h2o.i > run13.log 2>&1
mv h2o_out.csv h2o_out13.csv

sed -i '/initial_condition = 6576.8/c\initial_condition = 6668.9' h2o.i
../../projects/crane/crane-opt -i h2o.i > run14.log 2>&1
mv h2o_out.csv h2o_out14.csv

sed -i '/initial_condition = 6668.9/c\initial_condition = 7250.1' h2o.i
../../projects/crane/crane-opt -i h2o.i > run15.log 2>&1
mv h2o_out.csv h2o_out15.csv

sed -i '/initial_condition = 7250.1/c\initial_condition = 7354.7' h2o.i
../../projects/crane/crane-opt -i h2o.i > run16.log 2>&1
mv h2o_out.csv h2o_out16.csv
