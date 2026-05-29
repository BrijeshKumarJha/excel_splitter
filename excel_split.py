import pandas as pd
from pathlib import Path

def excel_splitter():
    file_input = input("Enter file name ")
    if not file_input.endswith(".xlsx"):
        file_input += ".xlsx"
    file_name = Path(file_input)
    if not file_name.exists() or not file_name.is_file():
        print("File not found or Invalid file name")

    try:
        df = pd.read_excel(file_name)
    except Exception as e:
        print(f"Could not read file. Error: {e}")
        return
        
    columns_list = df.columns.to_list()
    for index, column in enumerate(columns_list, start=1):
        print(f"{index} - {column} ")

    choice = input("Enter your choice number to filter data: ")

    try:
        selected_index = int(choice) - 1
        if 0<= selected_index <= len(columns_list):
            selected_column = columns_list[selected_index]
            output_dir = Path("Split_Files")
            output_dir.mkdir(exist_ok=True)

            unique_values = df[selected_column].unique()
            print(f"Found {len(unique_values)} unique values. Unique categories: {unique_values}")

            count = 0
            for value in unique_values:
                filtered_df = df[df[selected_column] == value]

                safe_value_name = str(value).replace(" ", "_").replace("/", "_")
                new_file_name = f"{selected_column}_{safe_value_name}.xlsx"
                new_file_path = output_dir / new_file_name

                filtered_df.to_excel(new_file_path, index=False)
                print(f"Creeated {new_file_name} containing {len(filtered_df)} rows")
                count += 1
            print(f"Done. Created {count} files, saved in {output_dir.name}")

        else:
            print("input out of range")
            return
    except:
        print("Invalid input, please enter a valid number")
        return
    
if __name__ == "__main__":
    excel_splitter()



