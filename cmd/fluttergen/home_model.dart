import 'home_data_model.dart';

class HomeModel {

	final bool success;
	final String message;
	final HomeDataModel data;

	HomeModel({
		required this.success,
		required this.message,
		required this.data,
	});

	factory HomeModel.fromJson(Map<String, dynamic> json) {
		return HomeModel(
			success: json["success"],
			message: json["message"],
			data: HomeDataModel.fromJson(json["data"]),
		);
	}

	Map<String, dynamic> toJson() {
		return {
			"success": this.success,
			"message": this.message,
			"data": this.data,
		};
	}

}
