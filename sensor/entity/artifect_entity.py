from dataclasses import dataclass


@dataclass
class DataIngestionArtiFact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str




class DataValidationArtiFact:...
class DataTransformationArtiFact:...
class ModelTrainingArtiFact:...
class ModelEvaluationArtiFact:...
class ModelPusherArtiFact:...