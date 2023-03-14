def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as new_data_file_name:
        result_dict = {"supply": 0, "buy": 0, "result": 0}
        for data in new_data_file_name:
            word, number = data.split(",")
            result_dict[word] += int(number)
            result_dict["result"] = result_dict["supply"] - result_dict["buy"]
    with open(report_file_name, "w") as upgrade_report_file_name:
        for key, value in result_dict.items():
            upgrade_report_file_name.write(f"{key},{value}\n")
