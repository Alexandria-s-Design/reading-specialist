"""Download all Jan Richardson resources: PDFs, videos, and images."""
import urllib.request
import os
import time
import sys

BASE = "https://www.janrichardsonreading.com/_files/ugd/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
ROOT = "C:/Users/ginja/reading-specialist"

# All 103+ PDFs organized by category
PDFS = {
    "resources/lesson-plans": {
        "Pre-A_Lesson_Plan.pdf": "7e0b43_595a463b2bd7408986daed8f2dfc2f88.pdf",
        "Pre-A_15min_Lesson_Plan.pdf": "7e0b43_f311e4c2ceb04e03ba21d4d16f4c680a.pdf",
        "Emergent_Lesson_Plan.pdf": "7e0b43_fb096178d72246b58822d24d412549c1.pdf",
        "Emergent_15min_Lesson_Plan.pdf": "7e0b43_699ecc3c12e2410a8566a95d35653261.pdf",
        "Early_Lesson_Plan.pdf": "7e0b43_305442f2200242e4badf490ea0126f23.pdf",
        "Early_15min_Lesson_Plan.pdf": "7e0b43_4ef3f9a12ce5440b9c9aaff043d3c528.pdf",
        "Transitional_Lesson_Plan.pdf": "7e0b43_342a632a10ab4aa3a3bbf4e88dc94470.pdf",
        "Transitional_Fluent_15min_Lesson_Plan.pdf": "7e0b43_e6cda4a125ef4c12852792d83665588e.pdf",
        "Fluent_Lesson_Plan.pdf": "7e0b43_07e33de024be48d2a320158ca89936a3.pdf",
        "Fluent_15min_Lesson_Plan.pdf": "7e0b43_1ee769d9626a4e0c9c96717157cfd410.pdf",
        "Lesson_Sample_Week_1.pdf": "7e0b43_c4afd751e1484a638a4b49776f18427a.pdf",
        "Lesson_Sample_Week_2.pdf": "7e0b43_3c432af070d64717b811b78bae73f2a7.pdf",
        "Lesson_Sample_Week_3.pdf": "7e0b43_0891acda977048d3985d717383653077.pdf",
    },
    "resources/spanish": {
        "Pre-A_Lectura_Guiada_2dias.pdf": "7e0b43_0078de3c37224ad19a5130651178d5cd.pdf",
        "Nivel_Principiante_3dias.pdf": "7e0b43_9bc1f86ecbf64d9b8066aecbe0c08c00.pdf",
        "Nivel_Emergente_3dias.pdf": "7e0b43_e03293016b3a47f3ab9c149b926253a5.pdf",
        "Lectura_Guiada_Transicional.pdf": "7e0b43_7a7a79319fbd4aaca36a9c6e334a99d9.pdf",
        "Spanish_Emergent_Lesson_Plan.pdf": "7e0b43_89169b2ca1fd4752ad2a13b719b64f5b.pdf",
        "Actividades_Trabajar_Con_Letras.pdf": "7e0b43_49f8acb29c754e25826fc68094d79357.pdf",
        "Spanish_ABC_Tracing_Book.pdf": "7e0b43_6e1a518ba9b24272a4953311421f755b.pdf",
        "Palabras_Alta_Frecuencia_Kinder_A1.pdf": "7e0b43_3bc94e7fa1434aa4b990f5c6018c3a6b.pdf",
        "Palabras_Primer_Grado_Primero.pdf": "7e0b43_f7916b5e5c91471f857306e49fdc9d85.pdf",
        "Palabras_Primer_Grado_G12.pdf": "7e0b43_0bede744a2b94e24b9cf40ad6598a464.pdf",
        "Palabras_Segundo.pdf": "7e0b43_23052dd8a1384bfca000ac772e949187.pdf",
        "Segundo_K20.pdf": "7e0b43_aa391b963d5b4da8acda22f534d6ddda.pdf",
        "Segundo_M28.pdf": "7e0b43_7808debd3e8547b689ca2cc519c680dd.pdf",
        "Segundo_N30.pdf": "7e0b43_fd04fe9daad94c7dbc1f9d43a7574f45.pdf",
        "Apendice_M_Sentimientos_Rasgos.pdf": "7e0b43_35812c7d809843e082a0ce574586fc3b.pdf",
        "Apendice_N_Tarjetas_Comprension.pdf": "7e0b43_f7c337ca96d547278f54475f29a842e8.pdf",
        "Vocabulary_Cards_Spanish.pdf": "7e0b43_27fbeeca3f23472884d083a5f20c9aaa.pdf",
        "STP_Cards_Spanish.pdf": "7e0b43_32dddd900da9483eaf6f61b94b7a2235.pdf",
        "Retelling_Scaffold_Spanish.pdf": "7e0b43_ee8d55a3f5924459adc937b73f777ca1.pdf",
        "Evaluaciones_Lectura_Guiada.pdf": "7e0b43_86304b03d813446cb13b7036074d56ea.pdf",
        "Evaluacion_Nivel_Emergente.pdf": "7e0b43_7126963aeb9f44789c0752e5309c813e.pdf",
        "Evaluacion_Nivel_Principiante.pdf": "7e0b43_b495aea6c6f04744891f4c88ad2721c7.pdf",
        "Evaluacion_Nivel_Transicional.pdf": "7e0b43_014347705c104d68ad268c3fbe9509b4.pdf",
        "Guia_Formacion_Letras.pdf": "7e0b43_87538ad518be43efbca8c7ac3e4d93ac.pdf",
        "Apendice_A_Por_Nivel_AJ.pdf": "7e0b43_8f49c3d1b481456cb8011ae6573f45e0.pdf",
    },
    "resources/french": {
        "Pre_A_Form_French.pdf": "7e0b43_cba881caf2a74b53a8956db03a578915.pdf",
        "Emergent_Form_French.pdf": "7e0b43_4877915802a84555b3168153786832c4.pdf",
        "Early_Form_Debutant_French.pdf": "7e0b43_65388b9eab354c10bc926e79938c8a25.pdf",
        "Transitional_Form_French.pdf": "7e0b43_a36e49a7adc448d7bab679f8d8c8ec86.pdf",
    },
    "resources/progress-charts": {
        "Grade_1_Progress_Chart.pdf": "7e0b43_2b8d21bf585141dc97b4a00a287e9cf1.pdf",
        "Grade_2_Progress_Chart.pdf": "7e0b43_1f6b128bc04c4553b829b1eb6185b47b.pdf",
        "Grade_3_Progress_Chart.pdf": "7e0b43_9fc0e19b2c3043f7ad9b0ccefd99a5a3.pdf",
        "Grade_4_Progress_Chart.pdf": "7e0b43_783ef512b56546b7869f2e9cd9cbacd7.pdf",
        "Grade_5_Progress_Chart.pdf": "7e0b43_013ac87e154f4d0c96f923b4bd88bacd.pdf",
        "School_Progress_Chart.pdf": "7e0b43_f2f2b58e99144a04b3e0e16953d80f4f.pdf",
        "Fillable_Reading_Progress_Chart.pdf": "7e0b43_b8c0300ea67c44d5a4e612e323c42059.pdf",
        "Writing_Progress_Monitoring_Chart.pdf": "7e0b43_ab23be36025b4292af4555293ac6289f.pdf",
        "Fluent_Assessment_Summary_Chart.pdf": "7e0b43_9788207aa2d7411eb3ebd01785e2b3ad.pdf",
        "Fillable_Word_Study_Inventory.pdf": "7e0b43_52bec0a235554d46a770b9713a931726.pdf",
        "Comprehension_Interview.pdf": "7e0b43_99317bd0358f46269c9ef796e48071c9.pdf",
        "Self_Assessment_GR_Rubric.pdf": "7e0b43_23e36bfb52a84b61b07e59086182a9e8.pdf",
        "Fidelity_Implementation_Checklist.pdf": "7e0b43_fc1fbe61170843edb256a3b85c14d943.pdf",
    },
    "resources/comprehension": {
        "How_to_Teach_Summarizing.pdf": "7e0b43_34197abd5bb947a9929112bc9d6ad8ac.pdf",
        "How_to_Teach_Cause_Effect.pdf": "7e0b43_3650c8d87cf2472b8774259a74fe8e43.pdf",
        "How_to_Teach_Making_Inferences.pdf": "7e0b43_af52c79efb824c949f1ea52b81f89f06.pdf",
        "How_to_Teach_Poetry_Analysis.pdf": "7e0b43_a42661a51628415488e9ba6cde2b4823.pdf",
        "How_to_Use_Asking_Questions.pdf": "7e0b43_5ec72a6bdc0f4e199a80e1824d039925.pdf",
        "How_to_Use_VIP_Strategy.pdf": "7e0b43_bc9c471f39ff401ebcad5352f0f88a09.pdf",
        "Comprehension_Strategies_Modules_Chart.pdf": "7e0b43_b1476055922b47b581abacceba826a0a.pdf",
        "GR_Comprehension_Scaffolds_WHare.pdf": "7e0b43_68317d98bc074739862ffc9a4886c903.pdf",
        "GR_vs_Book_Clubs.pdf": "7e0b43_1dddf5301910456eacf76844f657f3b8.pdf",
        "Tips_Managing_GR_Large_Classes.pdf": "7e0b43_cc219a9bc2ad442f9902968bc7e0edfa.pdf",
        "NSFGR_Professional_Study_Guide.pdf": "7e0b43_01aae29d94d54ac19f81131bae42b5b1.pdf",
    },
    "resources/cards": {
        "Vowel_Patterns_Cards.pdf": "7e0b43_0503036ed8c541aa82776ac8b9d69e7e.pdf",
        "Vowel_Patterns_Chart.pdf": "7e0b43_52a506b735a94ae2a08354b2cb5bfa99.pdf",
        "Decoding_Cards.pdf": "7e0b43_2f8be34243144df8bafda173208002b3.pdf",
        "STP_Cards.pdf": "7e0b43_38b290e41a6e41c899019d85b0aac636.pdf",
        "Cause_Effect_Cards.pdf": "7e0b43_411993fb28ad42928be32667e467cbe3.pdf",
        "Compare_Cards.pdf": "7e0b43_5f852fda0faf4aa2829b2fc0a12ecbca.pdf",
        "Contrast_Cards.pdf": "7e0b43_4da5071977f143808b57c8db1ea06e3f.pdf",
        "Question_Cards.pdf": "7e0b43_6ada45c0e0a74d8d8b935431d3e48581.pdf",
        "VIP_Cards.pdf": "7e0b43_a41384d942f64ad58d8b85f900cd0064.pdf",
        "Vocabulary_Cards.pdf": "7e0b43_789739e1685047a5a096db224b17a04e.pdf",
        "Testing_Strategy_Cards.pdf": "7e0b43_8233ec4e74044935be566e554c3b8458.pdf",
        "Early_Bookmarks.pdf": "7e0b43_270e31c4cdd64fd8bd0325bd740bdddc.pdf",
        "Advanced_Bookmarks.pdf": "7e0b43_ca79929b318940f38724ce170324e5cc.pdf",
        "Reciprocal_Teaching_Leader_Card.pdf": "7e0b43_59b450f9e1644ca5b4a0b7eabe3b1b62.pdf",
        "Reciprocal_Teaching.pdf": "7e0b43_c70a8de4b23442f58bfc1d23744fe74f.pdf",
    },
    "resources/word-study": {
        "Soundbox_Analogy_Chart_Template.pdf": "7e0b43_12d4ea47fb1f4e64a6f8c1947296340a.pdf",
        "Common_Affixes_Word_Endings.pdf": "7e0b43_3b62348ae27d4f3697b8afb144a2f115.pdf",
        "Easy_Prefixes_Suffixes.pdf": "7e0b43_9864aead0f5941498adc423f4d9b80b4.pdf",
        "Letter_Sound_Checklist.pdf": "7e0b43_b9f736d765e44803b4dd682edd1f3b27.pdf",
        "Alphabet_Chart.pdf": "7e0b43_6945d98ee6514a20b850ade66835f4cf.pdf",
        "My_Sound_Wall.pdf": "7e0b43_d5d270e4c246475d8cd56b27bfc9fb0d.pdf",
        "Personal_Word_Wall_Primary.pdf": "7e0b43_90fe964805174feaabdb050d75442e42.pdf",
        "Personal_Word_Wall_Intermediate.pdf": "7e0b43_784a8a2714764191a779306041fad56b.pdf",
        "New_Routine_Teaching_Sight_Words.pdf": "7e0b43_5b1047ae625d4d3983c45410c55c3fbe.pdf",
        "How_to_Teach_Guided_Word_Study.pdf": "7e0b43_5b9d05a3fe3c426c96f0e6a61eab33be.pdf",
    },
    "resources/reading-response": {
        "Reading_Response.pdf": "7e0b43_13849235d7c64c5988fd2bb45969b1b1.pdf",
        "Reading_Response_Choices_Fiction.pdf": "7e0b43_29b860c340fc4cd0b2501a28927fa302.pdf",
        "Reading_Response_Choices_Nonfiction.pdf": "7e0b43_7888a4f56da1402aa42f1a37d17bffe9.pdf",
        "5_Finger_Retelling.pdf": "7e0b43_da32bb45e5534273ab3577c70f5c94ca.pdf",
        "Shared_Retelling.pdf": "7e0b43_fd54dd9a20d746ab8e276bea517a96a1.pdf",
        "SWBS_Somebody_Wanted_But_So.pdf": "7e0b43_ea4383680d3b4bf8b9f5b10394d1c444.pdf",
    },
    "resources/writing": {
        "Handwriting_Journal.pdf": "7e0b43_dc86b86f5a3c458f97c4ff2008efab49.pdf",
        "Handwriting_Journal_K.pdf": "7e0b43_f9d2a888a23f4bdd88b2bd4d416f54f0.pdf",
        "Handwriting_Paper.pdf": "7e0b43_de9eb177660145d49dea4b80463728c3.pdf",
        "ABC_Tracing_Book.pdf": "7e0b43_93047210371f4c25a8b6559320e6df8e.pdf",
    },
    "resources/fluency": {
        "Punctuation_Rap.pdf": "7e0b43_ae04513c9501465babb900a4f6968b63.pdf",
    },
    "resources/other": {
        "First_20_Days_Reading_Workshop.pdf": "7e0b43_02e726498e194729a53e43d4a53bc0fa.pdf",
    },
    "resources/rise": {
        "RISE_Brochure.pdf": "7e0b43_87627091972a4e288e8a98fe2b03cb7e.pdf",
        "RISE_Action_Research_Study.pdf": "7e0b43_2870cb8f8ea548f88c0c782f0cf492d8.pdf",
        "RISE_Science_of_Reading_at_Work.pdf": "7e0b43_eab014cccc744563b9442be3344eced9.pdf",
        "RISE_Research_Validation.pdf": "7e0b43_d2bd5ba4b042414bb1e56b4bba45f68d.pdf",
        "RISE_Progress_Monitoring_Schedule.pdf": "7e0b43_76b116ebf2794f71874cbae57c0784aa.pdf",
        "RISE_Science_of_Reading.pdf": "7e0b43_65c2b4482bb548059670773a6905f708.pdf",
        "RISE_UP_New_Word_Study_Station.pdf": "7e0b43_9aa6d971783b45caa7ee6eebdfe552b4.pdf",
        "RISE_Common_Affixes_Word_Endings.pdf": "7e0b43_f7cd6e509e6e4decb036583ae32587f7.pdf",
        "RISE_Short_Vowel_Bookmark.pdf": "7e0b43_029b482ca36f441591c6a02721260476.pdf",
        "RISE_Vowel_Pattern_Cards.pdf": "7e0b43_2a95e59e0ee84a4e8751f483ecc2ddbf.pdf",
    },
    "resources/research": {
        "Next_Step_Framework_Science_of_Reading.pdf": "7e0b43_bd50870e39cd477f8402c8db3e284ec4.pdf",
        "Guided_Reading_and_Reading_Science.pdf": "7e0b43_1768c230701747fc8bb4c17bea44450e.pdf",
    },
    "resources/consultants": {
        "Consultant_Bio_1.pdf": "7e0b43_8e7b64060f644a308d37a1dc8034e38d.pdf",
        "Consultant_Bio_2.pdf": "7e0b43_6d901837f6e34913a165989f40371f36.pdf",
        "Consultant_Bio_3.pdf": "7e0b43_ddcbfa4865d840f38fc0f2c0983d3c06.pdf",
        "Consultant_Bio_4.pdf": "7e0b43_f7d1f9cf70454492af721928ffcce200.pdf",
        "Consultant_Bio_5.pdf": "7e0b43_8ac1aeea131644669cf31d2f71c6b9ab.pdf",
        "Bonnie_Porter_Heather_Micheli_Bio.pdf": "7e0b43_ed4ff7ac0c864322afb3a223b6e0dadd.pdf",
        "Courtney_Richardson_Bio.pdf": "7e0b43_12de58d633684ea8916b0befb503fa60.pdf",
        "Ellen_Lewis_Bio.pdf": "7e0b43_7722f603e86043238e222a9d02758b6e.pdf",
        "Pam_OLoughlin_Bio.pdf": "7e0b43_2221a29bb7d9437390c757dc4f002230.pdf",
    },
}

def download_file(url, path):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        resp = urllib.request.urlopen(req, timeout=30)
        data = resp.read()
        with open(path, 'wb') as f:
            f.write(data)
        return len(data)
    except Exception as e:
        return f"ERROR: {e}"

# Download all PDFs
total = sum(len(v) for v in PDFS.values())
count = 0
errors = 0

for folder, files in PDFS.items():
    folder_path = os.path.join(ROOT, folder)
    os.makedirs(folder_path, exist_ok=True)
    for filename, wix_id in files.items():
        count += 1
        filepath = os.path.join(folder_path, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
            print(f"[{count}/{total}] SKIP (exists): {filename}")
            continue
        url = BASE + wix_id
        result = download_file(url, filepath)
        if isinstance(result, int):
            print(f"[{count}/{total}] OK ({result:,} bytes): {folder}/{filename}")
        else:
            print(f"[{count}/{total}] FAIL: {folder}/{filename} - {result}")
            errors += 1
        time.sleep(0.3)

print(f"\nDone: {count} files attempted, {errors} errors")
