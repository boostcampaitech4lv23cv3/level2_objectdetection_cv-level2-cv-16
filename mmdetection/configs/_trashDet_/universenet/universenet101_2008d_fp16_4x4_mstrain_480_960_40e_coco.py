_base_ = [
    '../universenet/models/universenet101_2008d.py',
    '../_base_/datasets/coco_detection_aug_2.py',
    '../_base_/schedules/schedule_20e.py', '../_base_/default_runtime.py'
]

data = dict(samples_per_gpu=4)

optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(
    _delete_=True, grad_clip=dict(max_norm=35, norm_type=2))
lr_config = dict(warmup_iters=1000)
runner = dict(type='EpochBasedRunner', max_epochs=50)
fp16 = dict(loss_scale=512.)
