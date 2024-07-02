import os

def read_yolo_data_from_txt_file(file_path):
    yolo_data = []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split()
            integers = [int(val) for val in values[:len(values)-4]]
            floats = [float(val) for val in values[len(values)-4:]]
            yolo_data.append(integers + floats)
    return yolo_data

def split_data(yolo_data):
    result = []
    for data in yolo_data:
        integers = data[:len(data)-4]
        floats = data[len(data)-4:]
        for i in integers:
            result.append([i] + floats)
    return result

def write_yolo_data_to_txt_file(file_path, yolo_data):
    with open(file_path, 'w') as file:
        for data in yolo_data:
            line = ' '.join(str(val) for val in data) + '\n'
            file.write(line)

# ディレクトリ内のtxtファイルのパス
directory_path = '/Users/shibata/Desktop/hinoTopPy/validation'

# 任意の整数リストを指定
# 6と13~43を指定
# target_integers = [5,6,7,8]
target_integers = [num for num in range(14, 46)] + [13]

# ディレクトリ内のtxtファイルを読み込んでYoloデータを取得
for file_name in os.listdir(directory_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(directory_path, file_name)
        yolo_data = read_yolo_data_from_txt_file(file_path)
        processed_data = split_data(yolo_data)
        
        # 任意の整数リストに該当するデータのみ抽出
        filtered_data = [data for data in processed_data if data[0] in target_integers]
        
        # ファイルを上書き保存
        write_yolo_data_to_txt_file(file_path, filtered_data)
