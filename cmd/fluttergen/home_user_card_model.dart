
class HomeUserCardModel {

	final int card_number;
	final int expiry_month;
	final int expiry_year;
	final String name;
	final int cvv;

	HomeUserCardModel({
		required this.card_number,
		required this.expiry_month,
		required this.expiry_year,
		required this.name,
		required this.cvv,
	});

	factory HomeUserCardModel.fromJson(Map<String, dynamic> json) {
		return HomeUserCardModel(
			card_number: json["card_number"],
			expiry_month: json["expiry_month"],
			expiry_year: json["expiry_year"],
			name: json["name"],
			cvv: json["cvv"],
		);
	}

	Map<String, dynamic> toJson() {
		return {
			"card_number": this.card_number,
			"expiry_month": this.expiry_month,
			"expiry_year": this.expiry_year,
			"name": this.name,
			"cvv": this.cvv,
		};
	}

}
