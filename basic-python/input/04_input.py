pipeline_name = input("pipeline name ? : ")
batch_size = int(input("batch size ? : "))
retry_count = int(input("retry count ? : "))
maximum_record_attempt = batch_size * retry_count

print("==== Pipeline Configuration ====")
print(f"Pipeline : {pipeline_name}")
print(f"Batch Size : {batch_size}")
print(f"Retry Count : {retry_count}")
print(f"Maximum Records Attempted : {maximum_record_attempt}")

print("==== Variable Data Types ====")
print(type(pipeline_name))
print(type(batch_size))
print(type(retry_count))
print(type(maximum_record_attempt))

