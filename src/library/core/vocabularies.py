# -*- coding: utf-8 -*-

from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm


class ColorsVocabularyFactory:
    def __call__(self, context):
        provinces = [
            ("couleur", "Couleur"),
            ("noiretbanc", "Noir & Blanc"),
        ]
        terms = [
            SimpleTerm(value=pair[0], token=pair[0], title=pair[1])
            for pair in provinces
        ]
        return SimpleVocabulary(terms)


colorsvocabulary = ColorsVocabularyFactory()


class EventsdateVocabularyFactory:
    def __call__(self, context):
        provinces = [
            ("naissance", "Naissance"),
            ("mariage", "Mariage"),
            ("deces", "Décès"),
        ]
        terms = [
            SimpleTerm(value=pair[0], token=pair[0], title=pair[1])
            for pair in provinces
        ]
        return SimpleVocabulary(terms)


eventsdatevocabulary = ColorsVocabularyFactory()


class ProvincesVocabularyFactory:
    def __call__(self, context):
        provinces = [
            ("brabantwallon", "Brabant wallon"),
            ("hainaut", "Hainaut"),
            ("liege", "Liège"),
            ("luxembourg", "Luxembourg"),
            ("namur", "Namur"),
        ]
        terms = [
            SimpleTerm(value=pair[0], token=pair[0], title=pair[1])
            for pair in provinces
        ]
        return SimpleVocabulary(terms)


provincesvocabulary = ProvincesVocabularyFactory()


class MunicipalEntitiesVocabularyFactory:
    def __call__(self, context):
        municipal_entities = [
                ("aiseaupresles", "Aiseau-Presles"),
                ("amay", "Amay"),
                ("ambleve", "Amblève"),
                ("andenne", "Andenne"),
                ("anderlues", "Anderlues"),
                ("anhee", "Anhée"),
                ("ans", "Ans"),
                ("anthisnes", "Anthisnes"),
                ("antoing", "Antoing"),
                ("arlon", "Arlon"),
                ("assesse", "Assesse"),
                ("ath", "Ath"),
                ("attert", "Attert"),
                ("aubange", "Aubange"),
                ("aubel", "Aubel"),
                ("awans", "Awans"),
                ("aywaille", "Aywaille"),
                ("aaelen", "Baelen"),
                ("bassenge", "Bassenge"),
                ("bastogne", "Bastogne"),
                ("beaumont", "Beaumont"),
                ("beauraing", "Beauraing"),
                ("beauvechain", "Beauvechain"),
                ("beloeil", "Belœil"),
                ("berloz", "Berloz"),
                ("bernissart", "Bernissart"),
                ("bertogne", "Bertogne"),
                ("bertrix", "Bertrix"),
                ("beyneheusay", "Beyne-Heusay"),
                ("bievre", "Bièvre"),
                ("binche", "Binche"),
                ("blegny", "Blegny"),
                ("bouillon", "Bouillon"),
                ("boussu", "Boussu"),
                ("brainelalleud", "Braine-l'Alleud"),
                ("brainelechateau", "Braine-le-Château"),
                ("brainelecomte", "Braine-le-Comte"),
                ("braives", "Braives"),
                ("brugelette", "Brugelette"),
                ("brunehaut", "Brunehaut"),
                ("bullange", "Bullange"),
                ("burdinne", "Burdinne"),
                ("burg-Reuland", "Burg-Reuland"),
                ("butgenbach", "Butgenbach"),
                ("celles", "Celles"),
                ("cerfontaine", "Cerfontaine"),
                ("chapellelezherlaimont", "Chapelle-lez-Herlaimont"),
                ("charleroi", "Charleroi"),
                ("chastre", "Chastre"),
                ("chatelet", "Châtelet"),
                ("chaudfontaine", "Chaudfontaine"),
                ("chaumontgistoux", "Chaumont-Gistoux"),
                ("chievres", "Chièvres"),
                ("chimay", "Chimay"),
                ("chiny", "Chiny"),
                ("ciney", "Ciney"),
                ("clavier", "Clavier"),
                ("colfontaine", "Colfontaine"),
                ("comblainaupont", "Comblain-au-Pont"),
                ("comineswarneton", "Comines-Warneton"),
                ("courcelles", "Courcelles"),
                ("courtsaintetienne", "Court-Saint-Étienne"),
                ("couvin", "Couvin"),
                ("crisnee", "Crisnée"),
                ("dalhem", "Dalhem"),
                ("daverdisse", "Daverdisse"),
                ("dinant", "Dinant"),
                ("dison", "Dison"),
                ("doische", "Doische"),
                ("donceel", "Donceel"),
                ("dour", "Dour"),
                ("durbuy", "Durbuy"),
                ("ecaussinnes", "Écaussinnes"),
                ("eghezee", "Éghezée"),
                ("ellezelles", "Ellezelles"),
                ("enghien", "Enghien"),
                ("engis", "Engis"),
                ("erezee", "Érezée"),
                ("erquelinnes", "Erquelinnes"),
                ("esneux", "Esneux"),
                ("estaimpuis", "Estaimpuis"),
                ("estinnes", "Estinnes"),
                ("etalle", "Étalle"),
                ("eupen", "Eupen"),
                ("faimes", "Faimes"),
                ("farciennes", "Farciennes"),
                ("fauvillers", "Fauvillers"),
                ("fernelmont", "Fernelmont"),
                ("ferrieres", "Ferrières"),
                ("fexhelehautclocher", "Fexhe-le-Haut-Clocher"),
                ("flemalle", "Flémalle"),
                ("fleron", "Fléron"),
                ("fleurus", "Fleurus"),
                ("flobecq", "Flobecq"),
                ("floreffe", "Floreffe"),
                ("florennes", "Florennes"),
                ("florenville", "Florenville"),
                ("fontaineleveque", "Fontaine-l'Évêque"),
                ("fosseslaville", "Fosses-la-Ville"),
                ("frameries", "Frameries"),
                ("frasneslezanvaing", "Frasnes-lez-Anvaing"),
                ("froidchapelle", "Froidchapelle"),
                ("gedinne", "Gedinne"),
                ("geer", "Geer"),
                ("gembloux", "Gembloux"),
                ("genappe", "Genappe"),
                ("gerpinnes", "Gerpinnes"),
                ("gesves", "Gesves"),
                ("gouvy", "Gouvy"),
                ("gracehollogne", "Grâce-Hollogne"),
                ("grezdoiceau", "Grez-Doiceau"),
                ("habay", "Habay"),
                ("hamsurheurenalinnes", "Ham-sur-Heure-Nalinnes"),
                ("hamoir", "Hamoir"),
                ("hamois", "Hamois"),
                ("hannut", "Hannut"),
                ("hastiere", "Hastière"),
                ("havelange", "Havelange"),
                ("helecine", "Hélécine"),
                ("hensies", "Hensies"),
                ("herbeumont", "Herbeumont"),
                ("heron", "Héron"),
                ("herstal", "Herstal"),
                ("herve", "Herve"),
                ("honnelles", "Honnelles"),
                ("hotton", "Hotton"),
                ("houffalize", "Houffalize"),
                ("houyet", "Houyet"),
                ("huy", "Huy"),
                ("incourt", "Incourt"),
                ("ittre", "Ittre"),
                ("jalhay", "Jalhay"),
                ("jemeppesursambre", "Jemeppe-sur-Sambre"),
                ("jodoigne", "Jodoigne"),
                ("juprelle", "Juprelle"),
                ("jurbise", "Jurbise"),
                ("labruyere", "La Bruyère"),
                ("lacalamine", "La Calamine"),
                ("lahulpe", "La Hulpe"),
                ("larocheenardenne", "La Roche-en-Ardenne"),
                ("lasne", "Lasne"),
                ("leglise", "Léglise"),
                ("lens", "Lens"),
                ("leroeulx", "Le Rœulx"),
                ("lesbonsvillers", "Les Bons Villers"),
                ("lessines", "Lessines"),
                ("leuzeenhainaut", "Leuze-en-Hainaut"),
                ("libin", "Libin"),
                ("libramontchevigny", "Libramont-Chevigny"),
                ("liege", "Liège"),
                ("lierneux", "Lierneux"),
                ("limbourg", "Limbourg"),
                ("lincent", "Lincent"),
                ("lobbes", "Lobbes"),
                ("lontzen", "Lontzen"),
                ("lalouviere", "La Louvière"),
                ("malmedy", "Malmedy"),
                ("manage", "Manage"),
                ("manhay", "Manhay"),
                ("marcheenfamenne", "Marche-en-Famenne"),
                ("marchin", "Marchin"),
                ("martelange", "Martelange"),
                ("meixdevantvirton", "Meix-devant-Virton"),
                ("merbeslechateau", "Merbes-le-Château"),
                ("messancy", "Messancy"),
                ("mettet", "Mettet"),
                ("modave", "Modave"),
                ("momignies", "Momignies"),
                ("mons", "Mons"),
                ("montdelenclus", "Mont-de-l'Enclus"),
                ("montignyletilleul", "Montigny-le-Tilleul"),
                ("montsaintguibert", "Mont-Saint-Guibert"),
                ("morlanwelz", "Morlanwelz"),
                ("mouscron", "Mouscron"),
                ("musson", "Musson"),
                ("namur", "Namur"),
                ("nandrin", "Nandrin"),
                ("nassogne", "Nassogne"),
                ("neufchateau", "Neufchâteau"),
                ("neupre", "Neupré"),
                ("nivelles", "Nivelles"),
                ("ohey", "Ohey"),
                ("olne", "Olne"),
                ("onhaye", "Onhaye"),
                ("oreye", "Oreye"),
                ("orpjauche", "Orp-Jauche"),
                ("ottignieslouvainlaneuve", "Ottignies-Louvain-la-Neuve"),
                ("ouffet", "Ouffet"),
                ("oupeye", "Oupeye"),
                ("paliseul", "Paliseul"),
                ("pecq", "Pecq"),
                ("pepinster", "Pepinster"),
                ("peruwelz", "Péruwelz"),
                ("perwez", "Perwez"),
                ("philippeville", "Philippeville"),
                ("plombieres", "Plombières"),
                ("pontacelles", "Pont-à-Celles"),
                ("profondeville", "Profondeville"),
                ("quaregnon", "Quaregnon"),
                ("quevy", "Quévy"),
                ("quievrain", "Quiévrain"),
                ("raeren", "Raeren"),
                ("ramillies", "Ramillies"),
                ("rebecq", "Rebecq"),
                ("remicourt", "Remicourt"),
                ("rendeux", "Rendeux"),
                ("rixensart", "Rixensart"),
                ("rochefort", "Rochefort"),
                ("rouvroy", "Rouvroy"),
                ("rumes", "Rumes"),
                ("sainteode", "Sainte-Ode"),
                ("saintgeorgessurmeuse", "Saint-Georges-sur-Meuse"),
                ("saintghislain", "Saint-Ghislain"),
                ("sainthubert", "Saint-Hubert"),
                ("saintléger", "Saint-Léger"),
                ("saintnicolas", "Saint-Nicolas"),
                ("saintvith", "Saint-Vith"),
                ("sambreville", "Sambreville"),
                ("seneffe", "Seneffe"),
                ("seraing", "Seraing"),
                ("silly", "Silly"),
                ("sivryrance", "Sivry-Rance"),
                ("soignies", "Soignies"),
                ("sombreffe", "Sombreffe"),
                ("sommeleuze", "Somme-Leuze"),
                ("soumagne", "Soumagne"),
                ("spa", "Spa"),
                ("sprimont", "Sprimont"),
                ("stavelot", "Stavelot"),
                ("stoumont", "Stoumont"),
                ("tellin", "Tellin"),
                ("tenneville", "Tenneville"),
                ("theux", "Theux"),
                ("thimisterclermont", "Thimister-Clermont"),
                ("thuin", "Thuin"),
                ("tinlot", "Tinlot"),
                ("tintigny", "Tintigny"),
                ("tournai", "Tournai"),
                ("troisponts", "Trois-Ponts"),
                ("trooz", "Trooz"),
                ("tubize", "Tubize"),
                ("vauxsursure", "Vaux-sur-Sûre"),
                ("verlaine", "Verlaine"),
                ("verviers", "Verviers"),
                ("vielsalm", "Vielsalm"),
                ("villerslebouillet", "Villers-le-Bouillet"),
                ("villerslaville", "Villers-la-Ville"),
                ("viroinval", "Viroinval"),
                ("virton", "Virton"),
                ("vise", "Visé"),
                ("vressesursemois", "Vresse-sur-Semois"),
                ("waimes", "Waimes"),
                ("walcourt", "Walcourt"),
                ("walhain", "Walhain"),
                ("wanze", "Wanze"),
                ("waremme", "Waremme"),
                ("wasseiges", "Wasseiges"),
                ("waterloo", "Waterloo"),
                ("wavre", "Wavre"),
                ("welkenraedt", "Welkenraedt"),
                ("wellin", "Wellin"),
                ("yvoir", "Yvoir")]
        terms = [
            SimpleTerm(value=pair[0], token=pair[0], title=pair[1])
            for pair in municipal_entities
        ]
        return SimpleVocabulary(terms)


municipalentitiesvocabulary = MunicipalEntitiesVocabularyFactory()
