
# Scan how many trains and saved models already exist
PREDICT_IDX=$(ls runs/detect/ | grep predict | wc -l)
if ((PREDICT_IDX == 1)); then
    PREDICT_IDX=""
fi

MODEL_IDX=$(ls /models/ | wc -l)
if (( $MODEL_IDX == 0))
then
    MODEL="${MODEL:=yolov8n.pt}"
else
    MODEL_IDX_PRE=$(( $MODEL_IDX - 1 ))
    MODEL="${MODEL:=/models/best_$MODEL_IDX_PRE.pt}"
fi


yolo detect predict          \
    save_txt=true            \
    model="$MODEL"           \
    source=/detect/sources/  \
    imgsz=1088


# Copy all detections to all dir
cp runs/detect/predict$PREDICT_IDX /detect/all

# Compare detections with old labels and have the new ones live in ./new
cp /detect/all/*.txt /detect/new
find /labels -type f -execdir rm /detect/new/{} \;