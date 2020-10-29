# Instructions for installing dependencies for darknet on remote device

git clone https://github.com/pjreddie/darknet.git
cd darknet
make

#We already have CUDA installed so loading modules, including cuDNN
module load GCC/6.4.0-2.28 OpenMPI/2.1.2
module load CUDA/10.0.130 cuDNN/7.5.0.56-CUDA-10.0.130
#Now in darknet Makefile, change to GPU=1

# Need g++, cmake, make, wget, unzip.
# I will install opencv in ~/bin/opencv
cd bin

wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip
unzip opencv.zip
mv opencv-master opencv

# Create build directory for creating make files
mkdir -p build && cd build

# This line is the most important. Replace shius with your MSUID
cmake -D CMAKE_BUILD_TYPE=Release -D OPENCV_GENERATE_PKGCONFIG=YES -D CMAKE_INSTALL_PREFIX=/mnt/home/mengfanr/opencv/ ../opencv

# Finish installation
make -j4
make install

# Testing install
~/bin/opencv/bin/opencv_version
