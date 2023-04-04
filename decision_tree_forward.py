from klasifikasi_hewan import Vertebrata, Invertebrata

v_ordo = [
    'Apakah hewan tersebut hanya hidup di air?',
    'Apakah hewan tersebut hidup di air dan di darat?',
    'Apakah hewan tersebut bersisik?',
    'Apakah hewan tersebut memiliki sepasang sayap?',
    'Apakah hewan tersebut memiliki kelenjar susu?'
]

v_pisces = [
    'Apakah hewan tersebut tanpa rahang?',
    'Apakah hewan tersebut bertulang rawan?',
    'Apakah hewan tersebut bertulang keras?'
]

v_amfibia = [
    'Apakah hewan tersebut tidak memiliki ekor?',
    'Apakah hewan tersebut memiliki ekor?',
    'Apakah tidak memiliki tungkai?'
]

v_reptilia = [
    'Apakah hewan tersebut memiliki organ pelindung?',
    'Apakah hewan tersebut memiliki duri disepanjang tulang belakang?',
    'Apakah hewan tersebut ditutupi sisik?',
    'Apakah hewan tersebut memiliki rahang yang kuat?',
]

v_aves = [
    'Apakah hewan tersebut memiliki tiga jari kedepan?',
    'Apakah hewan tersebut memiliki tubuh yang kecil?'
]

v_mammalia = [
    'Apakah hewan tersebut memakan serangga?',
    'Apakah hewan tersebut memiliki sisik?',
    'Apakah hewan tersebut mampu terbang?',
    'Apakah hewan tersebut memiliki kantung?',
    'Apakah hewan tersebut memiliki hidung yang bisa digunakan untuk memegang sesuatu?',
    'Apakah hewan tersebut berkuku genap?'
]

i_ordo = [
    'Apakah hewan tersebut termasuk selomata?',
    'Apakah hewan tersebut bertubuh lunak?',
    'Apakah hewan tersebut dinding tubuhnya berkitin?',
    'Apakah hewan tersebut tidak memiliki dinding sel?',
    'Apakah hewan tersebut hanya hidup di udara?',
    'Apakah hewan tersebut bersifat aselomata?',
    'Apakah hewan tersebut berbentuk bulat panjang?',
    'Apakah hewan tersebut memiliki sifat knidosit?',
    'Apakah hewan tersebut tidak memiliki kepala dan tumbuh dalam sumbu oral-aboral?'
]

i_annelida = [
    'Apakah hewan tersebut seperti memiliki kaki-kaki di seluruh tubuh?',
    'Apakah hewan tersebut tubuhnya bersegmen?',
    'Apakah hewan tersebut mempunyai alat penghisap?'
]

i_mollusca = [
    'Apakah hewan tersebut memilih kaki pipih?',
    'Apakah hewan tersebut memiliki tubuh berukuran kecil dan ramping?',
    'Apakah hewan tersebut berkaki di kepala?',
    'Apakah hewan tersebut memiliki otot kaki yang dimodifikasi menjadi tangan?',
    'Apakah hewan tersebut memiliki kaki seperti kapak?'
]

i_anthropoda = [
    'Apakah hewan tersebut memiliki 2 atena?',
    'Apakah hewan tersebut mempunyai antena?',
    'Apakah hewan tersebut berbentuk panjang dan langsing?',
    'Apakah kakinya berjumlah 6 buah?'
]

i_protozoa = [
    'Apakah hewan tersebut berhabitat di perairan yang mengandung zat organik?',
    'Apakah hewan tersebut bersifat autotrof?',
    'Apakah hewan tersebut mempunyai spora?'
]

i_porifera = [
    'Apakah hewan tersebut memiliki rangka zat kapur?',
    'Apakah hewan tersebut hanya menempel pada permukaan keras?',
    'Apakah hewan tersebut tersusun dari serabut spongin?'
]

i_platyhelmithes = [
    'Apakah hewan tersebut mempunyai daya regenerasi yang sangat tinggi?',
    'Apakah hewan tersebut berbentuk seperti daun?',
    'Apakah hewan tersebut memiliki kait?'
]

i_nemathelminthes = [
    'Apakah tubuhnya tertutupi kutikulum?'
]

i_cnidaria = [
    'Apakah hewan tersebut berupa polip?',
    'Apakah hewan tersebut berbentuk seperti cawan?',
    'Apakah hewan tersebut berbentuk kotak?',
    'Apakah hewan tersebut memilik 8 lengan?',
    'Apakah hewan tersebut berbentuk menyerupai bunga?'
]

i_echinodermata = [
    'Apakah hewan tersebut memilik bergerak bebas?',
    'Apakah hewan tersebut bertangkai seperti bungai lili?',
    'Apakah hewan tersebut berbentuk pipih bundar?',
    'Apakah hewan tersebut hidupnya sesilis?',
    'Apakah hewan tersebut memiliki oral tetapi tidak ada anus?'
]

knowledge_base = {
    'Apakah hewan bertulang belakang?': {
        'Ya': {
            v_ordo[0]: {
                'Ya': {
                    v_pisces[0]: {
                        'Ya': Vertebrata['Kelas']['Pisces']['Ordo'].get('Agnatha')
                    },
                    v_pisces[1]: {
                        'Ya': Vertebrata['Kelas']['Pisces']['Ordo'].get('Chondrichthyes')
                    },
                    v_pisces[2]: {
                        'Ya': Vertebrata['Kelas']['Pisces']['Ordo'].get('Osteichthyes')
                    }
                }
            },
            v_ordo[1]: {
                'Ya': {
                    v_amfibia[0]: {
                        'Ya': Vertebrata['Kelas']['Amfibia']['Ordo'].get('Apoda')
                    },
                    v_amfibia[1]: {
                        'Ya': Vertebrata['Kelas']['Amfibia']['Ordo'].get('Caudata')
                    },
                    v_amfibia[2]: {
                        'Ya': Vertebrata['Kelas']['Amfibia']['Ordo'].get('Anura')
                    }
                }
            },
            v_ordo[2]: {
                'Ya': {
                    v_reptilia[0]: {
                        'Ya': Vertebrata['Kelas']['Reptilia']['Ordo'].get('Chenolia')
                    },
                    v_reptilia[1]: {
                        'Ya': Vertebrata['Kelas']['Reptilia']['Ordo'].get('Rhynchocephalia')
                    },
                    v_reptilia[2]: {
                        'Ya': Vertebrata['Kelas']['Reptilia']['Ordo'].get('Squamata')
                    },
                    v_reptilia[3]: {
                        'Ya': Vertebrata['Kelas']['Reptilia']['Ordo'].get('Crocodilia')
                    }
                }
            },
            v_ordo[3]: {
                'Ya': {
                    v_aves[0]: {
                        'Ya': Vertebrata['Kelas']['Aves']['Ordo'].get('Columbiformes')
                    },
                    v_aves[1]: {
                        'Ya': Vertebrata['Kelas']['Aves']['Ordo'].get('Coraciiformes')
                    }
                }
            },
            v_ordo[4]: {
                'Ya': {
                    v_mammalia[0]: {
                        'Ya': Vertebrata['Kelas']['Mammalia']['Ordo'].get('Insectivora')
                    },
                    v_mammalia[1]: {
                        'Ya': Vertebrata['Kelas']['Mammalia']['Ordo'].get('Pholidota')
                    },
                    v_mammalia[2]: {
                        'Ya': Vertebrata['Kelas']['Mammalia']['Ordo'].get('Chiroptera')
                    },
                    v_mammalia[3]: {
                        'Ya': Vertebrata['Kelas']['Mammalia']['Ordo'].get('Marsupialia')
                    },
                    v_mammalia[4]: {
                        'Ya': Vertebrata['Kelas']['Mammalia']['Ordo'].get('Proboscidae')
                    },
                    v_mammalia[5]: {
                        'Ya': Vertebrata['Kelas']['Mammalia']['Ordo'].get('Artiodactyle')
                    }
                }
            }
        },
        'Tidak': {
            i_ordo[0]: {
                i_annelida[0]: {
                    'Ya': Invertebrata['Kelas']['Annelida']['Ordo'].get('Polychaeta')
                },
                i_annelida[1]: {
                    'Ya': Invertebrata['Kelas']['Annelida']['Ordo'].get('Olygochaeta')
                },
                i_annelida[2]: {
                    'Ya': Invertebrata['Kelas']['Annelida']['Ordo'].get('Hirudinea')
                }
            },
            i_ordo[1]: {
                i_mollusca[0]: {
                    'Ya': Invertebrata['Kelas']['Mollusca']['Ordo'].get('Amphineura')
                },
                i_mollusca[1]: {
                    'Ya': Invertebrata['Kelas']['Mollusca']['Ordo'].get('Scaphopda')
                },
                i_mollusca[2]: {
                    'Ya': Invertebrata['Kelas']['Mollusca']['Ordo'].get('Gastropoda')
                },
                i_mollusca[3]: {
                    'Ya': Invertebrata['Kelas']['Mollusca']['Ordo'].get('Chepalopoda')
                },
                i_mollusca[4]: {
                    'Ya': Invertebrata['Kelas']['Mollusca']['Ordo'].get('Pelecypoda')
                }
            },
            i_ordo[2]: {
                i_anthropoda[0]: {
                    'Ya': Invertebrata['Kelas']['Anthropoda']['Ordo'].get('Crustaceae')
                },
                i_anthropoda[1]: {
                    'Ya': Invertebrata['Kelas']['Anthropoda']['Ordo'].get('Arachnoidea')
                },
                i_anthropoda[2]: {
                    'Ya': Invertebrata['Kelas']['Anthropoda']['Ordo'].get('Myriapoda')
                },
                i_anthropoda[3]: {
                    'Ya': Invertebrata['Kelas']['Anthropoda']['Ordo'].get('Insekta')
                }
            },
            i_ordo[3]: {
                i_protozoa[0]: {
                    'Ya': Invertebrata['Kelas']['Protozoa']['Ordo'].get('Rhizopoda')
                },
                i_protozoa[1]: {
                    'Ya': Invertebrata['Kelas']['Protozoa']['Ordo'].get('Flagellata')
                },
                i_protozoa[2]: {
                    'Ya': Invertebrata['Kelas']['Protozoa']['Ordo'].get('Sporozoa')
                }
            },
            i_ordo[4]: {
                i_porifera[0]: {
                    'Ya': Invertebrata['Kelas']['Porifera']['Ordo'].get('Calcarea')
                },
                i_porifera[1]: {
                    'Ya': Invertebrata['Kelas']['Porifera']['Ordo'].get('Hexactinellida')
                },
                i_porifera[2]: {
                    'Ya': Invertebrata['Kelas']['Porifera']['Ordo'].get('Demospongiae')
                }
            },
            i_ordo[5]: {
                i_platyhelmithes[0]: {
                    'Ya': Invertebrata['Kelas']['Platyhelminthes']['Ordo'].get('Tubellaria')
                },
                i_platyhelmithes[1]: {
                    'Ya': Invertebrata['Kelas']['Platyhelminthes']['Ordo'].get('Trematoda')
                },
                i_platyhelmithes[2]: {
                    'Ya': Invertebrata['Kelas']['Platyhelminthes']['Ordo'].get('Cestoda')
                }
            },
            i_ordo[6]: {
                i_nemathelminthes[0]: {
                    'Ya': Invertebrata['Kelas']['Nemathelminthes']['Ordo'].get('Nematoda')
                }
            },
            i_ordo[7]: {
                i_cnidaria[0]: {
                    'Ya': Invertebrata['Kelas']['Cnidaria']['Ordo'].get('Hydrozoa')
                },
                i_cnidaria[1]: {
                    'Ya': Invertebrata['Kelas']['Cnidaria']['Ordo'].get('Scyphozoa')
                },
                i_cnidaria[2]: {
                    'Ya': Invertebrata['Kelas']['Cnidaria']['Ordo'].get('Cubozoa')
                },
                i_cnidaria[3]: {
                    'Ya': Invertebrata['Kelas']['Cnidaria']['Ordo'].get('Staurozoa')
                },
                i_cnidaria[4]: {
                    'Ya': Invertebrata['Kelas']['Cnidaria']['Ordo'].get('Anthozoa')
                }
            },
            i_ordo[8]: {
                i_echinodermata[0]: {
                    'Ya': Invertebrata['Kelas']['Echinodermata']['Ordo'].get('Asteroidea')
                },
                i_echinodermata[1]: {
                    'Ya': Invertebrata['Kelas']['Echinodermata']['Ordo'].get('Crinoidea')
                },
                i_echinodermata[2]: {
                    'Ya': Invertebrata['Kelas']['Echinodermata']['Ordo'].get('Echinoidea')
                },
                i_echinodermata[3]: {
                    'Ya': Invertebrata['Kelas']['Echinodermata']['Ordo'].get('Holothuroidea')
                },
                i_echinodermata[4]: {
                    'Ya': Invertebrata['Kelas']['Echinodermata']['Ordo'].get('Ophiuroidea')
                }
            }
        }
    }
}
