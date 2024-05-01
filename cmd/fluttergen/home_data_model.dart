import 'home_user_card_model.dart';
import 'home_brands_model.dart';
import 'home_offers_model.dart';

class HomeDataModel {

	final HomeUserCardModel user_card;
	final List<HomeBrandsModel> brands;
	final List<HomeOffersModel> offers;

	HomeDataModel({
		required this.user_card,
		required this.brands,
		required this.offers,
	});

	factory HomeDataModel.fromJson(Map<String, dynamic> json) {
		return HomeDataModel(
			user_card: HomeUserCardModel.fromJson(json["user_card"]),
			brands: List<HomeBrandsModel>.from(json["brands"].map((x) => HomeBrandsModel.fromJson(x))),
			offers: List<HomeOffersModel>.from(json["offers"].map((x) => HomeOffersModel.fromJson(x))),
		);
	}

	Map<String, dynamic> toJson() {
		return {
			"user_card": this.user_card,
			"brands": this.brands,
			"offers": this.offers,
		};
	}

}
