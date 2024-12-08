
import boto3
def test_object_storage(bucket_name):
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        print("Bucket доступен.")
        return response
    except Exception as e:
        print(f"Ошибка доступа к Bucket: {e}")

# Вызов вашей функции
test_object_storage('bucketanna')