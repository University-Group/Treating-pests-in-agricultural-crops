from experta import *
from PIL import Image
import termcolor

apples_diseases_list = []
almonds_diseases_list = []			# مصفوفة أسماء الأمراض
apples_diseases_symptoms = []
# مصفوقة ثنائية كل سطر إجابات لأعراض المرض صاحب الاندكس المحدد
almonds_diseases_symptoms = []
apples_symptom_map = {} 			# إجابات المرض مفتاح ل اسم المرض
almonds_symptom_map = {}
d_desc_map = {}  			# اسم المرض مفتاح ل علاج المرض


def preprocess():
    global apples_diseases_list, almonds_diseases_list, apples_diseases_symptoms, almonds_diseases_symptoms, apples_symptom_map, almonds_symptom_map, d_desc_map
    diseases = open("apples_diseases.txt")
    diseases_t = diseases.read()
    apples_diseases_list = diseases_t.split("\n")
    diseases.close()

    for disease in apples_diseases_list:
        if(disease == ""):
            continue
        disease_s_file = open("Apples Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        apples_diseases_symptoms.append(s_list)
        apples_symptom_map[str(s_list)] = disease
        disease_s_file.close()

        disease_s_file = open("Disease treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()

    diseases2 = open("almonds_diseases.txt")
    diseases_t2 = diseases2.read()
    almonds_diseases_list = diseases_t2.split("\n")
    diseases2.close()

    for disease2 in almonds_diseases_list:
        if(disease2 == ""):
            continue
        disease_s_file2 = open("Almonds Disease symptoms/" + disease2 + ".txt")
        disease_s_data2 = disease_s_file2.read()
        s_list2 = disease_s_data2.split("\n")
        almonds_diseases_symptoms.append(s_list2)
        almonds_symptom_map[str(s_list2)] = disease2
        disease_s_file2.close()

        disease_s_file2 = open("Disease treatments/" + disease2 + ".txt")
        disease_s_data2 = disease_s_file2.read()
        d_desc_map[disease2] = disease_s_data2
        disease_s_file2.close()


def get_treatment(disease):
    return d_desc_map[disease]


def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_treatment(id_disease)
    print("")
    print(termcolor.colored("The most probable disease that you have is",
          "green"), " %s\n" % (id_disease))
    print(termcolor.colored(
        "The best treatment of this disease is given below :\n", "red"))
    print(disease_details+"\n")

    if(id_disease == "Armillaria mellea"):
        im = Image.open("images/Armillaria mellea.jpg")
        im.show(title="Armillaria mellea")
    if(id_disease == "Cytospora"):
        im = Image.open("images/Cytospora.jpg")
        im.show(title="Cytospora")
    if(id_disease == "Gymnosporangium sabinae"):
        im = Image.open("images/Gymnosporangium sabinae.jpg")
        im.show(title="Gymnosporangium sabinae")
    if(id_disease == "Monilia fructigena"):
        im = Image.open("images/Monilia fructigena.jpg")
        im.show(title="Monilia fructigena")
    if(id_disease == "Monilia laxa"):
        im = Image.open("images/Monilia laxa.jpg")
        im.show(title="Monilia laxa")
    if(id_disease == "Podosphaera leucotricha"):
        im = Image.open("images/Podosphaera leucotricha.jpg")
        im.show(title="Podosphaera leucotricha")
    if(id_disease == "Spilocaea pomi"):
        im = Image.open("images/Spilocaea pomi.jpg")
        im.show(title="Spilocaea pomi")
    if(id_disease == "Taphrina deformans"):
        im = Image.open("images/Taphrina deformans.jpg")
        im.show(title="Taphrina deformans")
    if(id_disease == "Tranzschelia pruni spinosae"):
        im = Image.open("images/Tranzschelia pruni spinosae.jpg")
        im.show(title="Tranzschelia pruni spinosae")
    if(id_disease == "Verticillium dahliae"):
        im = Image.open("images/Verticillium dahliae.jpg")
        im.show(title="Verticillium dahliae")


class Greetings(KnowledgeEngine):

    @Rule(Fact(crop='apples'), NOT(Fact(yellowLeaves=W())), salience=14)
    def symptom_0(self):
        self.declare(Fact(yellowLeaves=input(
            "1- Yellow leaves? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(lowLeavesDensity=W())), salience=13)
    def symptom_1(self):
        self.declare(Fact(lowLeavesDensity=input(
            "2- low leaves density? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(earlyFallLeaves=W())), salience=12)
    def symptom_2(self):
        self.declare(Fact(earlyFallLeaves=input(
            "3- Early fall of leaves? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(leavesBlade=W())), salience=11)
    def symptom_3(self):
        self.declare(Fact(leavesBlade=input(
            "4- Reduction of the leaves blade with wrinkling and the appearance of fungus growths? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(soptsBumps=W())), salience=10)
    def symptom_4(self):
        self.declare(Fact(soptsBumps=input(
            "5- Spots with small bumps on the top surface of the leaf? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(flowerWiltBlack=W())), salience=9)
    def symptom_5(self):
        self.declare(Fact(flowerWiltBlack=input(
            "6- Flowers wilting and blackening? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(blackRootPeel=W())), salience=8)
    def symptom_6(self):
        self.declare(Fact(blackRootPeel=input(
            "7- Is the root peel stained brown and then black? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(spotBranchUcler=W())), salience=7)
    def symptom_7(self):
        self.declare(Fact(spotBranchUcler=input(
            "8- Spots on the branches that turn into sores? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(gummySores=W())), salience=6)
    def symptom_8(self):
        self.declare(Fact(gummySores=input(
            "9- Gummy secretions from sores? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(spotOlives=W())), salience=5)
    def symptom_9(self):
        self.declare(Fact(spotOlives=input(
            "10- spots like olives on fruits? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(fruitDryUp=W())), salience=4)
    def symptom_10(self):
        self.declare(Fact(fruitDryUp=input("11- Infected fruits dry up? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(softRotFruit=W())), salience=3)
    def symptom_11(self):
        self.declare(Fact(softRotFruit=input(
            "12- Superficial, round brown spots (soft rot) on fruits? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(roughTexture=W())), salience=2)
    def symptom_12(self):
        self.declare(Fact(roughTexture=input(
            "13- Large fruits have a rough texture? : ")))

    @Rule(Fact(crop='apples'), NOT(Fact(fruitFungus=W())), salience=1)
    def symptom_13(self):
        self.declare(Fact(fruitFungus=input(
            "14- Large fruits are covered with fungus? : ")))

    @Rule(Fact(crop='apples'), Fact(yellowLeaves="yes"),
          Fact(blackRootPeel="yes"),
          Fact(lowLeavesDensity="yes"),
          Fact(fruitFungus="no"),
          Fact(roughTexture="no"),
          Fact(softRotFruit="no"),
          Fact(fruitDryUp="no"),
          Fact(earlyFallLeaves="no"),
          Fact(leavesBlade="no"),
          Fact(soptsBumps="no"),
          Fact(flowerWiltBlack="no"),
          Fact(spotBranchUcler="no"),
          Fact(gummySores="no"),
          Fact(spotOlives="no"),
          NOT(Fact(AShowed=W())), salience=8)
    def disease_0(self):
        self.declare(Fact(disease="Armillaria mellea"))
        im = Image.open("images/Armillaria mellea.jpg")
        im.show()
        # print("leaf rust")
        self.declare(Fact(AShowed="yes"))

    @Rule(Fact(crop='apples'), Fact(yellowLeaves="no"),
          Fact(blackRootPeel="no"),
          Fact(lowLeavesDensity="no"),
          Fact(fruitFungus="no"),
          Fact(roughTexture="no"),
          Fact(softRotFruit="no"),
          Fact(fruitDryUp="no"),
          Fact(leavesBlade="no"),
          Fact(soptsBumps="no"),
          Fact(flowerWiltBlack="yes"),
          Fact(spotBranchUcler="yes"),
          Fact(gummySores="no"),
          Fact(spotOlives="yes"),
          NOT(Fact(BShowed=W())), salience=5)
    def disease_1(self):
        self.declare(Fact(disease="Spilocaea pomi"))
        im = Image.open("images/Spilocaea pomi.jpg")
        im.show()
        # print("leaf rust")
        self.declare(Fact(BShowed="yes"))

    @Rule(Fact(crop='apples'), Fact(yellowLeaves="no"),
          Fact(blackRootPeel="no"),
          Fact(lowLeavesDensity="no"),
          OR(Fact(fruitFungus="yes"), Fact(roughTexture="yes")),
          Fact(softRotFruit="no"),
          Fact(fruitDryUp="no"),
          Fact(earlyFallLeaves="no"),
          Fact(leavesBlade="yes"),
          Fact(soptsBumps="no"),
          Fact(flowerWiltBlack="no"),
          Fact(spotBranchUcler="no"),
          Fact(gummySores="no"),
          Fact(spotOlives="no"),
          NOT(Fact(CShowed=W())), salience=0)
    def disease_2(self):
        self.declare(Fact(disease="Podosphaera leucotricha"))
        im = Image.open("images/Podosphaera leucotricha.jpg")
        im.show()
        # print("leaf rust")
        self.declare(Fact(CShowed="yes"))

    @Rule(Fact(crop='apples'), Fact(yellowLeaves="no"),
          Fact(blackRootPeel="no"),
          Fact(lowLeavesDensity="no"),
          Fact(fruitFungus="no"),
          Fact(roughTexture="no"),
          OR(Fact(softRotFruit="yes"), Fact(fruitDryUp="yes")),
          Fact(earlyFallLeaves="no"),
          Fact(leavesBlade="no"),
          Fact(soptsBumps="no"),
          Fact(flowerWiltBlack="no"),
          Fact(spotBranchUcler="yes"),
          Fact(gummySores="yes"),
          Fact(spotOlives="no"),
          NOT(Fact(DShowed=W())), salience=3)
    def disease_3(self):
        self.declare(Fact(disease="Monilia fructigena"))
        im = Image.open("images/Monilia fructigena.jpg")
        im.show()
        # print("leaf rust")
        self.declare(Fact(DShowed="yes"))

    @Rule(Fact(crop='apples'), Fact(yellowLeaves="no"),
          Fact(blackRootPeel="no"),
          Fact(lowLeavesDensity="no"),
          Fact(fruitFungus="no"),
          Fact(roughTexture="no"),
          Fact(softRotFruit="no"),
          Fact(fruitDryUp="no"),
          Fact(earlyFallLeaves="no"),
          Fact(leavesBlade="no"),
          Fact(soptsBumps="yes"),
          Fact(flowerWiltBlack="no"),
          Fact(spotBranchUcler="no"),
          Fact(gummySores="no"),
          Fact(spotOlives="no"),
          NOT(Fact(CShowed=W())), salience=10)
    def disease_4(self):
        self.declare(Fact(disease="Gymnosporangium sabinae"))
        im = Image.open("images/Gymnosporangium sabinae.jpg")
        im.show()
        # print("leaf rust")
        self.declare(Fact(CShowed="yes"))

    @Rule(Fact(crop='apples'), Fact(yellowLeaves="no"),
          Fact(blackRootPeel="no"),
          Fact(lowLeavesDensity="no"),
          Fact(fruitFungus="no"),
          Fact(roughTexture="no"),
          Fact(softRotFruit="no"),
          Fact(fruitDryUp="no"),
          Fact(earlyFallLeaves="no"),
          Fact(leavesBlade="no"),
          Fact(soptsBumps="no"),
          Fact(flowerWiltBlack="no"),
          Fact(spotBranchUcler="no"),
          Fact(gummySores="no"),
          Fact(spotOlives="no"),
          NOT(Fact(CShowed=W())), salience=-1)
    def disease_5(self):
        self.declare(Fact(disease="Disease Not Detected"))

    @Rule(Fact(crop='apples'), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = get_treatment(id_disease)
        print("")
        if(id_disease == "Disease Not Detected"):
            print(termcolor.colored("Your plant is healthy", "blue"))
        else:
            print(termcolor.colored(
                "The most probable disease that the plant has is", "green"), "%s\n" % (id_disease))
        print(termcolor.colored(
            "The best treatment of this disease is given below :\n", "red"))
        print(disease_details+"\n")

    @Rule(Fact(crop='apples'), Fact(yellowLeaves=MATCH.yellowLeaves),
          Fact(blackRootPeel=MATCH.blackRootPeel),
          Fact(lowLeavesDensity=MATCH.lowLeavesDensity),
          Fact(fruitFungus=MATCH.fruitFungus),
          Fact(roughTexture=MATCH.roughTexture),
          Fact(softRotFruit=MATCH.softRotFruit),
          Fact(fruitDryUp=MATCH.fruitDryUp),
          Fact(earlyFallLeaves=MATCH.earlyFallLeaves),
          Fact(leavesBlade=MATCH.leavesBlade),
          Fact(soptsBumps=MATCH.soptsBumps),
          Fact(flowerWiltBlack=MATCH.flowerWiltBlack),
          Fact(spotBranchUcler=MATCH.spotBranchUcler),
          Fact(gummySores=MATCH.gummySores),
          Fact(spotOlives=MATCH.spotOlives), NOT(Fact(disease=MATCH.disease)), salience=-999)
    def not_matched2(self, yellowLeaves, blackRootPeel, lowLeavesDensity, fruitFungus, roughTexture, softRotFruit, fruitDryUp, earlyFallLeaves, leavesBlade, soptsBumps,
                     flowerWiltBlack, spotBranchUcler, gummySores, spotOlives):
        print(termcolor.colored(
            "\nDid not find any disease that matches given exact symptoms", "yellow"))
        lis = [yellowLeaves, lowLeavesDensity, earlyFallLeaves, leavesBlade, soptsBumps, flowerWiltBlack,
               blackRootPeel, spotBranchUcler, gummySores, spotOlives, fruitDryUp, softRotFruit, roughTexture, fruitFungus]

        max_count = 0
        max_disease = ""
        for key, val in apples_symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if(temp_list[j] == lis[j] and lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)

    @Rule(Fact(crop='almonds'), NOT(Fact(yellowSpot=W())), salience=14)
    def symptom_16(self):
        self.declare(Fact(yellowSpot=input(
            "1- Yellowish spots on the upper surface of the leaf? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(orangePustules=W())), salience=13)
    def symptom_17(self):
        self.declare(Fact(orangePustules=input(
            "2- Orange pustules on the underside of the leaf? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(incSize=W())), salience=12)
    def symptom_18(self):
        self.declare(Fact(incSize=input(
            "3- Increase in size of leaf? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(yellowLeaves=W())), salience=11)
    def symptom_19(self):
        self.declare(Fact(yellowLeaves=input(
            "4- Yellow leaves? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(curlLeaf=W())), salience=10)
    def symptom_20(self):
        self.declare(Fact(curlLeaf=input(
            "5- The leaf curls? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(droopLeaf=W())), salience=9)
    def symptom_21(self):
        self.declare(Fact(droopLeaf=input(
            "6- wilting and drooping leafs? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(redLeaf=W())), salience=8)
    def symptom_22(self):
        self.declare(Fact(redLeaf=input(
            "7- The leaf turns red? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(earlyFallLeaves=W())), salience=7)
    def symptom_23(self):
        self.declare(Fact(earlyFallLeaves=input(
            "8- Early fall of leaves? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(fruitDryUp=W())), salience=6)
    def symptom_24(self):
        self.declare(Fact(fruitDryUp=input("9- Infected fruits dry up? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(softRotFruit=W())), salience=5)
    def symptom_25(self):
        self.declare(Fact(softRotFruit=input(
            "10- Superficial, round brown spots (soft rot) on fruits? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(wound=W())), salience=4)
    def symptom_26(self):
        self.declare(Fact(wound=input(
            "11- An open, non-healing wound on the trunk and branches? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(spotBranchUcler=W())), salience=3)
    def symptom_27(self):
        self.declare(Fact(spotBranchUcler=input(
            "12- Spots on the branches that turn into sores? : ")))

    @Rule(Fact(crop='almonds'), NOT(Fact(gummySores=W())), salience=2)
    def symptom_28(self):
        self.declare(Fact(gummySores=input(
            "13- Gummy secretions from sores? : ")))

    @Rule(Fact(crop='almonds'), Fact(spotBranchUcler="yes"),
          Fact(gummySores="yes"),
          OR(Fact(fruitDryUp="yes"), Fact(softRotFruit="yes")),
          Fact(yellowSpot="no"),
          Fact(orangePustules="no"),
          Fact(incSize="no"),
          Fact(curlLeaf="no"),
          Fact(redLeaf="no"),
          Fact(droopLeaf="no"),
          Fact(yellowLeaves="no"),
          Fact(earlyFallLeaves="no"),
          Fact(wound="no"),
          NOT(Fact(Gshowed=W())))
    def disease_6(self):
        self.declare(Fact(disease="Monilia laxa"))
        im = Image.open("images/Monilia laxa.jpg")
        im.show()
        # print("leaf rust")
        self.declare(Fact(Gshowed="yes"))

    @Rule(Fact(crop='almonds'), Fact(spotBranchUcler="no"),
          Fact(gummySores="no"),
          Fact(fruitDryUp="no"),
          Fact(softRotFruit="no"),
          AND(Fact(yellowSpot="yes"), Fact(orangePustules="yes")),
          Fact(incSize="no"),
          Fact(curlLeaf="no"),
          Fact(redLeaf="no"),
          Fact(droopLeaf="no"),
          Fact(yellowLeaves="no"),
          Fact(earlyFallLeaves="no"),
          Fact(wound="no"),
          NOT(Fact(Hshowed=W())))
    def disease_7(self):
        self.declare(Fact(disease="Tranzschelia pruni spinosae"))
        im = Image.open("images/Tranzschelia pruni spinosae.jpg")
        im.show()
        # print("leaf rust")
        self.declare(Fact(Hshowed="yes"))

    @Rule(Fact(crop='almonds'), Fact(spotBranchUcler="no"),
          Fact(gummySores="no"),
          Fact(fruitDryUp="no"),
          Fact(softRotFruit="no"),
          Fact(yellowSpot="no"),
          Fact(orangePustules="no"),
          Fact(incSize="yes"),
          Fact(curlLeaf="yes"),
          Fact(redLeaf="yes"),
          Fact(droopLeaf="no"),
          Fact(yellowLeaves="no"),
          Fact(earlyFallLeaves="no"),
          Fact(wound="no"),
          NOT(Fact(Ishowed=W())))
    def disease_8(self):
        self.declare(Fact(disease="Taphrina deformans"))
        im = Image.open("images/Taphrina deformans.jpg")
        im.show()
        # print("leaf rust")
        self.declare(Fact(Ishowed="yes"))

    @Rule(Fact(crop='almonds'), Fact(spotBranchUcler="no"),
          Fact(gummySores="no"),
          Fact(fruitDryUp="no"),
          Fact(softRotFruit="no"),
          Fact(yellowSpot="no"),
          Fact(orangePustules="no"),
          Fact(incSize="no"),
          Fact(curlLeaf="no"),
          Fact(redLeaf="no"),
          Fact(droopLeaf="yes"),
          Fact(yellowLeaves="yes"),
          Fact(earlyFallLeaves="yes"),
          Fact(wound="no"),
          NOT(Fact(Gshowed=W())))
    def disease_9(self):
        self.declare(Fact(disease="Verticillium dahliae"))
        im = Image.open("images/Verticillium dahliae.jpg")
        im.show()
        # print("leaf rust")
        self.declare(Fact(Gshowed="yes"))

    @Rule(Fact(crop='almonds'), Fact(spotBranchUcler="no"),
          Fact(gummySores="no"),
          Fact(fruitDryUp="no"),
          Fact(softRotFruit="no"),
          Fact(yellowSpot="no"),
          Fact(orangePustules="no"),
          Fact(incSize="no"),
          Fact(curlLeaf="no"),
          Fact(redLeaf="no"),
          Fact(droopLeaf="no"),
          Fact(yellowLeaves="no"),
          Fact(earlyFallLeaves="no"),
          Fact(wound="yes"),
          NOT(Fact(Kshowed=W())))
    def disease_10(self):
        self.declare(Fact(disease="Cytospora"))
        im = Image.open("images/Cytospora.jpg")
        im.show()
        # print("leaf rust")
        self.declare(Fact(Kshowed="yes"))

    @Rule(Fact(crop='almonds'), Fact(spotBranchUcler="no"),
          Fact(gummySores="no"),
          Fact(fruitDryUp="no"),
          Fact(softRotFruit="no"),
          Fact(yellowSpot="no"),
          Fact(orangePustules="no"),
          Fact(incSize="no"),
          Fact(curlLeaf="no"),
          Fact(redLeaf="no"),
          Fact(droopLeaf="no"),
          Fact(yellowLeaves="no"),
          Fact(earlyFallLeaves="no"),
          Fact(wound="no"),
          NOT(Fact(Lshowed=W())))
    def disease_11(self):
        self.declare(Fact(disease="Disease Not Detected"))

    @Rule(Fact(crop='almonds'), Fact(disease=MATCH.disease), salience=-998)
    def diseasealmond(self, disease):
        print("")
        id_disease = disease
        disease_details = get_treatment(id_disease)
        print("")
        if(id_disease == "Disease Not Detected"):
            print(termcolor.colored("Your plant is healthy", "blue"))
        else:
            print(termcolor.colored(
                "The most probable disease that the plant has is", "green"), "%s\n" % (id_disease))
        print(termcolor.colored(
            "The best treatment of this disease is given below :\n", "red"))
        print(disease_details+"\n")

    @Rule(Fact(crop='almonds'), Fact(spotBranchUcler=MATCH.spotBranchUcler),
          Fact(gummySores=MATCH.gummySores),
          Fact(fruitDryUp=MATCH.fruitDryUp),
          Fact(softRotFruit=MATCH.softRotFruit),
          Fact(yellowSpot=MATCH.yellowSpot),
          Fact(orangePustules=MATCH.orangePustules),
          Fact(incSize=MATCH.incSize),
          Fact(curlLeaf=MATCH.curlLeaf),
          Fact(redLeaf=MATCH.redLeaf),
          Fact(droopLeaf=MATCH.droopLeaf),
          Fact(yellowLeaves=MATCH.yellowLeaves),
          Fact(earlyFallLeaves=MATCH.earlyFallLeaves),
          Fact(wound=MATCH.wound),
          NOT(Fact(disease=MATCH.disease)), salience=-999)
    def not_matched(self, spotBranchUcler, gummySores, fruitDryUp, softRotFruit, yellowSpot, orangePustules, incSize,
                    curlLeaf, redLeaf, droopLeaf, yellowLeaves, earlyFallLeaves, wound):
        print(termcolor.colored(
            "\nDid not find any diseasessss that matches given exact symptoms", "yellow"))
        lis = [yellowSpot, orangePustules, incSize, yellowLeaves, curlLeaf,
               droopLeaf, redLeaf, earlyFallLeaves, fruitDryUp, softRotFruit, wound,
               spotBranchUcler, gummySores]
        max_count = 0
        max_disease = ""
        for key, val in almonds_symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if(lis[j] == "yes" and temp_list[j] == lis[j]):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)


if __name__ == "__main__":
    preprocess()
    engine = Greetings()
    while(1):
        engine.reset()  # Prepare the engine for the execution.
        print("")
        print("Expert System in Detecting Plants Diseases")
        print("Please answer a few questions about the plan conditions")
        print("")
        f = Fact(crop=input("Is the agricultural crop of almonds or apples?"))
        engine.declare(f)
        engine.run()  # Run it!
        print("Would you like to diagnose some other symptoms?")
        if "no" in input().lower():
            exit()
        # print(engine.facts)
