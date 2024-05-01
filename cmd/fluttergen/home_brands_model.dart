
class HomeBrandsModel {

	final int id;
	final String name;
	final String logo;

	HomeBrandsModel({
		required this.id,
		required this.name,
		required this.logo,
	});

	factory HomeBrandsModel.fromJson(Map<String, dynamic> json) {
		return HomeBrandsModel(
			id: json["id"],
			name: json["name"],
			logo: json["logo"],
		);
	}

	Map<String, dynamic> toJson() {
		return {
			"id": this.id,
			"name": this.name,
			"logo": this.logo,
		};
	}

}
