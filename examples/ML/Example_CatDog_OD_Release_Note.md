Model version: 1.01c rev2
Release date: 04/01/2024
Dataset: My_ODCatsAndDogs
Model type: Object Detection 
Model Type: Keras Yolov8 
Source Model: yolo_v8_m_backbone_coco

- For TensorFlow Models use the [saved model CLI](https://www.tensorflow.org/guide/saved_model#details_of_the_savedmodel_command_line_interface)to find input and output tensors
Input Tensor: 
  inputs['input'] tensor_info:
      dtype: DT_FLOAT
      shape: (-1, 1024, 1024, 3)
      name: serving_default_input:0

Output Tensor:
    outputs['boxes'] tensor_info:
      dtype: DT_FLOAT
      shape: (-1, 100, 4)
      name: StatefulPartitionedCall:0

  outputs['classes'] tensor_info:
      dtype: DT_INT64
      shape: (-1, 100)
      name: StatefulPartitionedCall:1

  outputs['confidence'] tensor_info:
      dtype: DT_FLOAT
      shape: (-1, 100)
      name: StatefulPartitionedCall:2
      
  outputs['num_detections'] tensor_info:
      dtype: DT_INT32
      shape: (-1)
      name: StatefulPartitionedCall:3
Method name is: tensorflow/serving/predict

Recommended confidence threshold: 0.5
Class map: {1: 'dog', 2: 'cat'}
Description: finds dogs and cats in a 1024x1024 image. 
Changes from last release: Dataset was updated with more corgi images