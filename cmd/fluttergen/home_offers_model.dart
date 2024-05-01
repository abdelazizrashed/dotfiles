
class HomeOffersModel {

	final int id;
	final String name;
	final String image;
	final String end_date;
	final int discount_percent;
	final String brand;

	HomeOffersModel({
		required this.id,
		required this.name,
		required this.image,
		required this.end_date,
		required this.discount_percent,
		required this.brand,
	});

	factory HomeOffersModel.fromJson(Map<String, dynamic> json) {
		return HomeOffersModel(
			id: json["id"],
			name: json["name"],
			image: json["image"],
			end_date: json["end_date"],
			discount_percent: json["discount_percent"],
			brand: json["brand"],
		);
	}

	Map<String, dynamic> toJson() {
		return {
			"id": this.id,
			"name": this.name,
			"image": this.image,
			"end_date": this.end_date,
			"discount_percent": this.discount_percent,
			"brand": this.brand,
		};
	}

}
