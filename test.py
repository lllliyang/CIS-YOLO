import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(r'')

    metrics = model.val(
        data=r'',
        split='test',
        imgsz=640,
        batch=16,
        project=r'',
        name='',
        save=True,
        save_txt=True,
        save_conf=False
    )
