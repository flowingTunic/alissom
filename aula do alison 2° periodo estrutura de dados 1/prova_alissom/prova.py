lista =[]
dados = {
    "cpf0": {
        "nome": "Antonio",
        "idade": 57,
        "salario": 3205.05
    },
    "cpf1": {
        "nome": "Andreia",
        "idade": 40,
        "salario": 1696.23
    },
    "cpf2": {
        "nome": "Valdemar",
        "idade": 29,
        "salario": 10884.58
    },
    "cpf3": {
        "nome": "Nayra",
        "idade": 37,
        "salario": 2504.32
    },
    "cpf4": {
        "nome": "Luiz",
        "idade": 22,
        "salario": 4179.59
    },
    "cpf5": {
        "nome": "Olga",
        "idade": 19,
        "salario": 5999.72
    },
    "cpf6": {
        "nome": "Emmanuel",
        "idade": 65,
        "salario": 8007.48
    },
    "cpf7": {
        "nome": "Leonor",
        "idade": 31,
        "salario": 7874.21
    },
    "cpf8": {
        "nome": "Valentine",
        "idade": 52,
        "salario": 10902.53
    },
    "cpf9": {
        "nome": "Apolo",
        "idade": 58,
        "salario": 5444.92
    },
    "cpf10": {
        "nome": "Kimi",
        "idade": 45,
        "salario": 6476.92
    },
    "cpf11": {
        "nome": "Yaqi",
        "idade": 68,
        "salario": 7273.04
    },
    "cpf12": {
        "nome": "Jayden",
        "idade": 34,
        "salario": 9626.1
    },
    "cpf13": {
        "nome": "Lea",
        "idade": 52,
        "salario": 7833.82
    },
    "cpf14": {
        "nome": "Noe",
        "idade": 60,
        "salario": 6139.42
    },
    "cpf15": {
        "nome": "Isaias",
        "idade": 65,
        "salario": 8795.33
    },
    "cpf16": {
        "nome": "Lua",
        "idade": 36,
        "salario": 10338.97
    },
    "cpf17": {
        "nome": "Juan",
        "idade": 47,
        "salario": 1070.15
    },
    "cpf18": {
        "nome": "Anny",
        "idade": 21,
        "salario": 6092.26
    },
    "cpf19": {
        "nome": "Aaron",
        "idade": 34,
        "salario": 8852.02
    },
    "cpf20": {
        "nome": "Richard",
        "idade": 19,
        "salario": 6814.3
    },
    "cpf21": {
        "nome": "Jefferson",
        "idade": 20,
        "salario": 1694.95
    },
    "cpf22": {
        "nome": "Kauan",
        "idade": 29,
        "salario": 5908.01
    },
    "cpf23": {
        "nome": "Ivy",
        "idade": 48,
        "salario": 3591.01
    },
    "cpf24": {
        "nome": "Haniela",
        "idade": 36,
        "salario": 4931.61
    },
    "cpf25": {
        "nome": "Manel",
        "idade": 25,
        "salario": 2458.1
    },
    "cpf26": {
        "nome": "Telmo",
        "idade": 68,
        "salario": 4194.91
    },
    "cpf27": {
        "nome": "Sujana",
        "idade": 69,
        "salario": 3733.23
    },
    "cpf28": {
        "nome": "Olinda",
        "idade": 47,
        "salario": 8432.84
    },
    "cpf29": {
        "nome": "Dominika",
        "idade": 57,
        "salario": 9870.99
    },
    "cpf30": {
        "nome": "Teotonio",
        "idade": 49,
        "salario": 7488.0
    },
    "cpf31": {
        "nome": "Dalia",
        "idade": 50,
        "salario": 6752.7
    },
    "cpf32": {
        "nome": "Djelissa",
        "idade": 41,
        "salario": 8176.06
    },
    "cpf33": {
        "nome": "Rania",
        "idade": 29,
        "salario": 5058.72
    },
    "cpf34": {
        "nome": "Rodolfo",
        "idade": 46,
        "salario": 8706.73
    },
    "cpf35": {
        "nome": "Brahim",
        "idade": 52,
        "salario": 5554.51
    },
    "cpf36": {
        "nome": "Artyom",
        "idade": 20,
        "salario": 3683.65
    },
    "cpf37": {
        "nome": "Yassna",
        "idade": 47,
        "salario": 1217.04
    },
    "cpf38": {
        "nome": "Irene",
        "idade": 51,
        "salario": 10827.45
    },
    "cpf39": {
        "nome": "Ming",
        "idade": 58,
        "salario": 7128.63
    },
    "cpf40": {
        "nome": "Lamarana",
        "idade": 33,
        "salario": 8951.33
    },
    "cpf41": {
        "nome": "Tomas",
        "idade": 60,
        "salario": 7799.56
    },
    "cpf42": {
        "nome": "Azael",
        "idade": 45,
        "salario": 5700.02
    },
    "cpf43": {
        "nome": "Patricia",
        "idade": 51,
        "salario": 8584.37
    },
    "cpf44": {
        "nome": "Arnaldo",
        "idade": 35,
        "salario": 1135.85
    },
    "cpf45": {
        "nome": "Mario",
        "idade": 70,
        "salario": 3792.42
    },
    "cpf46": {
        "nome": "Martim",
        "idade": 57,
        "salario": 1819.96
    },
    "cpf47": {
        "nome": "Emma",
        "idade": 70,
        "salario": 5785.36
    },
    "cpf48": {
        "nome": "Abdul",
        "idade": 60,
        "salario": 8548.24
    },
    "cpf49": {
        "nome": "Mariam",
        "idade": 68,
        "salario": 10118.37
    },
    "cpf50": {
        "nome": "Valentina",
        "idade": 21,
        "salario": 3857.34
    },
    "cpf51": {
        "nome": "Debora",
        "idade": 56,
        "salario": 7779.32
    },
    "cpf52": {
        "nome": "Dario",
        "idade": 19,
        "salario": 5990.78
    },
    "cpf53": {
        "nome": "Januario",
        "idade": 39,
        "salario": 2781.33
    },
    "cpf54": {
        "nome": "Absalao",
        "idade": 56,
        "salario": 3836.41
    },
    "cpf55": {
        "nome": "Nuno",
        "idade": 58,
        "salario": 9300.15
    },
    "cpf56": {
        "nome": "Dennis",
        "idade": 37,
        "salario": 6549.03
    },
    "cpf57": {
        "nome": "Georgi",
        "idade": 21,
        "salario": 7425.37
    },
    "cpf58": {
        "nome": "Catalin",
        "idade": 47,
        "salario": 10695.87
    },
    "cpf59": {
        "nome": "Viktoria",
        "idade": 20,
        "salario": 8924.35
    },
    "cpf60": {
        "nome": "Patricio",
        "idade": 49,
        "salario": 1334.17
    },
    "cpf61": {
        "nome": "Letizia",
        "idade": 52,
        "salario": 3574.67
    },
    "cpf62": {
        "nome": "Neusa",
        "idade": 35,
        "salario": 7424.93
    },
    "cpf63": {
        "nome": "Clara",
        "idade": 21,
        "salario": 6441.68
    },
    "cpf64": {
        "nome": "Jamie",
        "idade": 68,
        "salario": 7588.22
    },
    "cpf65": {
        "nome": "Deise",
        "idade": 43,
        "salario": 5466.76
    },
    "cpf66": {
        "nome": "Ariele",
        "idade": 55,
        "salario": 4293.94
    },
    "cpf67": {
        "nome": "Catalina",
        "idade": 31,
        "salario": 6231.71
    },
    "cpf68": {
        "nome": "Mathilde",
        "idade": 33,
        "salario": 3595.9
    },
    "cpf69": {
        "nome": "Caio",
        "idade": 44,
        "salario": 8718.39
    },
    "cpf70": {
        "nome": "Daria",
        "idade": 51,
        "salario": 4976.81
    },
    "cpf71": {
        "nome": "Damien",
        "idade": 52,
        "salario": 1784.93
    },
    "cpf72": {
        "nome": "Silvestre",
        "idade": 25,
        "salario": 5337.69
    },
    "cpf73": {
        "nome": "Angela",
        "idade": 25,
        "salario": 5981.29
    },
    "cpf74": {
        "nome": "Christian",
        "idade": 70,
        "salario": 10120.56
    },
    "cpf75": {
        "nome": "Aaliyah",
        "idade": 64,
        "salario": 8789.82
    },
    "cpf76": {
        "nome": "Rui",
        "idade": 49,
        "salario": 4306.27
    },
    "cpf77": {
        "nome": "Cassandra",
        "idade": 65,
        "salario": 1643.52
    },
    "cpf78": {
        "nome": "Cinara",
        "idade": 30,
        "salario": 3064.65
    },
    "cpf79": {
        "nome": "Nadia",
        "idade": 60,
        "salario": 1702.87
    },
    "cpf80": {
        "nome": "Helton",
        "idade": 55,
        "salario": 1531.14
    },
    "cpf81": {
        "nome": "Genesia",
        "idade": 21,
        "salario": 8207.85
    },
    "cpf82": {
        "nome": "Paulo",
        "idade": 54,
        "salario": 1246.03
    },
    "cpf83": {
        "nome": "Arian",
        "idade": 21,
        "salario": 7977.66
    },
    "cpf84": {
        "nome": "Kailany",
        "idade": 23,
        "salario": 1392.67
    },
    "cpf85": {
        "nome": "Noa",
        "idade": 61,
        "salario": 1801.33
    },
    "cpf86": {
        "nome": "Alisha",
        "idade": 62,
        "salario": 4136.17
    },
    "cpf87": {
        "nome": "Amanda",
        "idade": 63,
        "salario": 4430.08
    },
    "cpf88": {
        "nome": "Michele",
        "idade": 70,
        "salario": 3892.58
    },
    "cpf89": {
        "nome": "Jadir",
        "idade": 59,
        "salario": 5860.66
    },
    "cpf90": {
        "nome": "Aleksandr",
        "idade": 67,
        "salario": 7548.07
    },
    "cpf91": {
        "nome": "Michael",
        "idade": 65,
        "salario": 5149.24
    },
    "cpf92": {
        "nome": "Jasmine",
        "idade": 49,
        "salario": 2973.83
    },
    "cpf93": {
        "nome": "Alexandro",
        "idade": 60,
        "salario": 9423.37
    },
    "cpf94": {
        "nome": "Karine",
        "idade": 59,
        "salario": 8354.02
    },
    "cpf95": {
        "nome": "Emily",
        "idade": 36,
        "salario": 4345.09
    },
    "cpf96": {
        "nome": "Maira",
        "idade": 53,
        "salario": 2586.61
    },
    "cpf97": {
        "nome": "Aliana",
        "idade": 53,
        "salario": 8971.28
    },
    "cpf98": {
        "nome": "Allana",
        "idade": 20,
        "salario": 4364.17
    },
    "cpf99": {
        "nome": "Ivana",
        "idade": 41,
        "salario": 8377.6
    }
}
lista.append(dados)
def print_sorted(x):
    x.sort()
    for elem in x:
        print(elem)
print_sorted(lista)