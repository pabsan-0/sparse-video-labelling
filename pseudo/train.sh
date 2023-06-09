
# Scan how many trains and saved models already exist
TRAIN_IDX=$(( $(ls runs/detect/ | grep train | wc -l) ))
if ((TRAIN_IDX == 1)); then
    TRAIN_IDX=""
fi

MODEL_IDX=$(ls /models/ | wc -l)
if (( $MODEL_IDX == 0))
then
    MODEL="${MODEL:=yolov8n.pt}"
else
    MODEL_IDX_PRE=$(( $MODEL_IDX - 1 ))
    MODEL="${MODEL:=/models/best_$MODEL_IDX_PRE.pt}"
fi


# Build dataset
cp -t /dataset/train /labels/*
mv -t /dataset/test $(find pseudo/dataset/train -type f | shuf -n 100)

source macros.sh  ## import f_unlink_frames, f_link_frames
f_unlink_frames /dataset/train
f_unlink_frames /dataset/test
f_link_frames /frames /dataset/train
f_link_frames /frames /dataset/test


yolo train data=/dataset/dataset.yaml \
    amp=False                         \
    imgsz=1080                        \
    model="$MODEL"                    \
    pretrained=True                   


# move relevant assets to wherever I want them 
# cp runs/detect/train$TRAIN_IDX/weights/last.pt  /models/last_$MODEL_IDX.pt  ## the script becomes unreliable if exporting both
cp runs/detect/train$TRAIN_IDX/weights/best.pt  /models/best_$MODEL_IDX.pt 
