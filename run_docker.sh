

sudo docker build -t dockername -f /home/ayagoz/cluster-utils/docker/tv_reg.dockerfile .

sudo docker run -dit     --name dockername      -p 8789:8789     -v /home/ayagoz:/workspace dockername

./cluster_utils/docker/build.sh neuro-dl 28-12-2017 neuroml



