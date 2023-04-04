from klasifikasi_hewan import Vertebrata, Invertebrata

knowledge_base_ = {
    "Apakah hewan bertulang belakang?": {
        "Ya": {
            "Apakah hewan tersebut hanya hidup di air?": {
                "Ya": {
                    "Apakah hewan tersebut tanpa rahang?": {
                        "Ya": [
                            Vertebrata["Kelas"]["Pisces"]["Ordo"].get(
                                "Agnatha")
                        ],
                        "Tidak": {
                            "Apakah hewan tersebut bertulang rawan?": {
                                "Ya": Vertebrata["Kelas"]["Pisces"]["Ordo"].get("Chondrichthyes"),
                                "Tidak": {
                                    "Apakah hewan tersebut bertulang keras?": {
                                        "Ya": Vertebrata["Kelas"]["Pisces"]["Ordo"].get("Osteichthyes"),
                                        "Tidak": "Klasifikasi salah!"
                                    }
                                }
                            }
                        }
                    }
                },
                "Tidak": {
                    "Apakah hewan tersebut hidup di air dan di darat?": {
                        "Ya": {
                            "Apakah hewan tersebut tidak memiliki ekor?": {
                                "Ya": Vertebrata["Kelas"]["Amfibia"]["Ordo"].get("Anura"),
                                "Tidak": {
                                    "Apakah hewan tersebut memiliki ekor?": {
                                        "Ya": Vertebrata["Kelas"]["Amfibia"]["Ordo"].get("Caudata"),
                                        "Tidak": {
                                            "Apakah tidak memiliki tungkai?": {
                                                "Ya": Vertebrata["Kelas"]["Amfibia"]["Ordo"].get("Apoda"),
                                                "Tidak": "Klasifikasi salah!"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "Tidak": {
                            "Apakah hewan tersebut bersisik?": {
                                "Ya": {
                                    "Apakah hewan tersebut memiliki organ pelindung?": {
                                        "Ya": Vertebrata["Kelas"]["Reptilia"]["Ordo"].get("Chenolia"),
                                        "Tidak": {
                                            "Apakah hewan tersebut ditutupi sisik?": {
                                                "Ya": Vertebrata["Kelas"]["Reptilia"]["Ordo"].get("Squamata"),
                                                "Tidak": {
                                                    "Apakah hewan tersebut memiliki rahang yang kuat?": {
                                                        "Ya": Vertebrata["Kelas"]["Reptilia"]["Ordo"].get("Crocodilia"),
                                                        "Tidak": {
                                                            "Apakah hewan tersebut memiliki duri disepanjang tulang belakang?": {
                                                                "Ya": Vertebrata["Kelas"]["Reptilia"]["Ordo"].get("Rhynchocephalia"),
                                                                "Tidak": "Klasifikasi salah!"
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "Tidak": {
                                    "Apakah hewan tersebut memiliki sepasang sayap?": {
                                        "Ya": {
                                            "Apakah hewan tersebut memiliki tiga jari kedepan?": {
                                                "Ya": Vertebrata["Kelas"]["Aves"]["Ordo"].get("Columbiformes"),
                                                "Tidak": {
                                                    "Apakah hewan tersebut memiliki tubuh yang kecil?": {
                                                        "Ya": Vertebrata["Kelas"]["Aves"]["Ordo"].get("Coraciiformes"),
                                                        "Tidak": "Klasifikasi salah!"
                                                    }
                                                }
                                            }
                                        },
                                        "Tidak": {
                                            "Apakah hewan tersebut memiliki kelenjar susu?": {
                                                "Ya": {
                                                    "Apakah hewan tersebut memakan serangga?": {
                                                        "Ya": Vertebrata["Kelas"]["Mammalia"]["Ordo"].get("Insectivora"),
                                                        "Tidak": {
                                                            "Apakah hewan tersebut memiliki sisik?": {
                                                                "Ya": Vertebrata["Kelas"]["Mammalia"]["Ordo"].get("Pholidota"),
                                                                "Tidak": {
                                                                    "Apakah hewan tersebut mampu terbang?": {
                                                                        "Ya": Vertebrata["Kelas"]["Mammalia"]["Ordo"].get("Chiroptera"),
                                                                        "Tidak": {
                                                                            "Apakah hewan tersebut memiliki kantung?": {
                                                                                "Ya": Vertebrata["Kelas"]["Mammalia"]["Ordo"].get("Marsupialia"),
                                                                                "Tidak": {
                                                                                    "Apakah hewan tersebut memiliki hidung yang bisa digunakan untuk memegang sesuatu?": {
                                                                                        "Ya": Vertebrata["Kelas"]["Mammalia"]["Ordo"].get("Proboscidae"),
                                                                                        "Tidak": {
                                                                                            "Apakah hewan tersebut berkuku genap?": {
                                                                                                "Ya":
                                                                                                    Vertebrata["Kelas"]["Mammalia"]["Ordo"].get(
                                                                                                        "Artiodactyla"),
                                                                                                "Tidak": "Klasifikasi salah!"
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "Tidak": {
            "Apakah hewan tersebut termasuk selomata?": {
                "Ya": {
                    "Apakah hewan tersebut seperti memiliki kaki-kaki di seluruh tubuh?": {
                        "Ya": Invertebrata['Kelas']["Annelida"]['Ordo'].get("Polychaeta"),
                        "Tidak": {
                            "Apakah hewan tersebut tubuhnya bersegmen?": {
                                "Ya": Invertebrata['Kelas']["Annelida"]['Ordo'].get("Olygochaeta"),
                                "Tidak": {
                                    "Apakah hewan tersebut mempunyai alat penghisap?": {
                                        "Ya": Invertebrata['Kelas']["Annelida"]['Ordo'].get("Hirudinea"),
                                        "Tidak": "Klasifikasi Salah!"
                                    }
                                }
                            }
                        }
                    }
                },
                "Tidak": {
                    "Apakah hewan tersebut bertubuh lunak?": {
                        "Ya": {
                            "Apakah hewan tersebut memilih kaki pipih?": {
                                "Ya": Invertebrata['Kelas']["Mollusca"]['Ordo'].get("Amphineura"),
                                "Tidak": {
                                    "Apakah hewan tersebut memiliki tubuh berukuran kecil dan ramping?": {
                                        "Ya": Invertebrata['Kelas']["Mollusca"]['Ordo'].get("Scaphopda"),
                                        "Tidak": {
                                            "Apakah hewan tersebut berkaki di kepala?": {
                                                "Ya": Invertebrata['Kelas']["Mollusca"]['Ordo'].get("Gastropoda"),
                                                "Tidak": {
                                                    "Apakah hewan tersebut memiliki otot kaki yang dimodifikasi menjadi tangan?": {
                                                        "Ya": Invertebrata['Kelas']["Mollusca"]['Ordo'].get("Chepalopoda"),
                                                        "Tidak": {
                                                            "Apakah hewan tersebut memiliki kaki seperti kapak?": {
                                                                "Ya": Invertebrata['Kelas']["Mollusca"]['Ordo'].get("Pelecypoda"),
                                                                "Tidak": "Klasifikasi salah!"
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }, "Tidak": {
                            "Apakah hewan tersebut dinding tubuhnya berkitin?": {
                                "Ya": {
                                    "Apakah hewan tersebut memiliki 2 atena?": {
                                        "Ya": Invertebrata['Kelas']["Anthropoda"]['Ordo'].get("Crustaceae"),
                                        "Tidak": {
                                            "Apakah hewan tersebut mempunyai antena?": {
                                                "Ya": Invertebrata['Kelas']["Anthropoda"]['Ordo'].get("ArachTidakidea"),
                                                "Tidak": {
                                                    "Apakah hewan tersebut berbentuk panjang dan langsing?": {
                                                        "Ya": Invertebrata['Kelas']["Anthropoda"]['Ordo'].get("Myriapoda"),
                                                        "Tidak": {
                                                            "Apakah kakinya berjumlah 6 buah?": {
                                                                "Ya": Invertebrata['Kelas']["Anthropoda"]['Ordo'].get("Insekta"),
                                                                "Tidak": "Klasifikasi salah!"
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }, "Tidak": {
                                    "Apakah hewan tersebut tidak memiliki dinding sel?": {
                                        "Ya": {
                                            "Apakah hewan tersebut berhabitat di perairan yang mengandung zat organik?": {
                                                "Ya": Invertebrata['Kelas']["Protozoa"]['Ordo'].get("Rhizopoda"),
                                                "Tidak": {
                                                    "Apakah hewan tersebut bersifat autotrof?": {
                                                        "Ya": Invertebrata['Kelas']["Protozoa"]['Ordo'].get("Flagellata"),
                                                        "Tidak": {
                                                            "Apakah hewan tersebut mempunyai spora?": {
                                                                "Ya": Invertebrata['Kelas']["Protozoa"]['Ordo'].get("Sporozoa"),
                                                                "Tidak": "Klasifikasi salah!"
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "Tidak": {
                                            "Apakah hewan tersebut hanya hidup di udara?": {
                                                "Ya": {
                                                    "Apakah hewan tersebut memiliki rangka zat kapur?": {
                                                        "Ya": Invertebrata['Kelas']["Porifera"]['Ordo'].get("Calcarea"),
                                                        "Tidak": {
                                                            "Apakah hewan tersebut hanya menempel pada permukaan keras?": {
                                                                "Ya": Invertebrata['Kelas']["Porifera"]['Ordo'].get("Hexactinellida"),
                                                                "Tidak": {
                                                                    "Apakah hewan tersebut tersusun dari serabut spongin?": {
                                                                        "Ya": Invertebrata['Kelas']["Porifera"]['Ordo'].get("Demospongiae"),
                                                                        "Tidak": "Klasifikasi salah!"
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "Tidak": {
                                                    "Apakah hewan tersebut bersifat aselomata?": {
                                                        "Ya": {
                                                            "Apakah hewan tersebut mempunyai daya regenerasi yang sangat tinggi?": {
                                                                "Ya": Invertebrata['Kelas']["Platyhelminthes"]['Ordo'].get("Turbellaria"),
                                                                "Tidak": {
                                                                    "Apakah hewan tersebut berbentuk seperti daun?": {
                                                                        "Ya": Invertebrata['Kelas']["Platyhelminthes"]['Ordo'].get("Trematoda"),
                                                                        "Tidak": {
                                                                            "Apakah hewan tersebut memiliki kait?": {
                                                                                "Ya": Invertebrata['Kelas']["Platyhelminthes"]['Ordo'].get("Cestoda"),
                                                                                "Tidak": "Klasifikasi salah!"
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        },
                                                        "Tidak": {
                                                            "Apakah hewan tersebut berbentuk bulat panjang?": {
                                                                "Ya": {
                                                                    "Apakah tubuhnya tertutupi kutikulum?": {
                                                                        "Ya": Invertebrata['Kelas']["Nemathelminthes"]['Ordo'].get("Nematoda"),
                                                                        "Tidak": "Klasifikasi salah!"
                                                                    }
                                                                },
                                                                "Tidak": {
                                                                    "Apakah hewan tersebut memiliki sifat knidosit?": {
                                                                        "Ya": {
                                                                            "Apakah hewan tersebut berupa polip?": {
                                                                                "Ya": Invertebrata['Kelas']["Cnidaria"]['Ordo'].get("Hydrozoa"),
                                                                                "Tidak": {
                                                                                    "Apakah hewan tersebut berbentuk seperti cawan?": {
                                                                                        "Ya": Invertebrata['Kelas']["Cnidaria"]['Ordo'].get("Scyphozoa"),
                                                                                        "Tidak": {
                                                                                            "Apakah hewan tersebut berbentuk kotak?": {
                                                                                                "Ya": Invertebrata['Kelas']["Cnidaria"]['Ordo'].get("Cubozoa"),
                                                                                                "Tidak": {
                                                                                                    "Apakah hewan tersebut memilik 8 lengan?": {
                                                                                                        "Ya": Invertebrata['Kelas']["Cnidaria"]['Ordo'].get("Staurozoa"),
                                                                                                        "Tidak": {
                                                                                                            "Apakah hewan tersebut berbentuk menyerupai bunga?": {
                                                                                                                "Ya": Invertebrata['Kelas']["Cnidaria"]['Ordo'].get("Anthozoa"),
                                                                                                                "Tidak": "Klasifikasi salah!"
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        },
                                                                        "Tidak": {
                                                                            "Apakah hewan tersebut tidak memiliki kepala dan tumbuh dalam sumbu oral-aboral?": {
                                                                                "Ya": {
                                                                                    "Apakah hewan tersebut memilik bergerak bebas?": {
                                                                                        "Ya": Invertebrata['Kelas']["Echinodermata"]['Ordo'].get("Asteroidea"),
                                                                                        "Tidak": {
                                                                                            "Apakah hewan tersebut bertangkai seperti bungai lili?": {
                                                                                                "Ya": Invertebrata['Kelas']["Echinodermata"]['Ordo'].get("CriTidakidea"),
                                                                                                "Tidak": {
                                                                                                    "Apakah hewan tersebut berbentuk pipih bundar?": {
                                                                                                        "Ya": Invertebrata['Kelas']["Echinodermata"]['Ordo'].get("EchiTidakidea"),
                                                                                                        "Tidak": {
                                                                                                            "Apakah hewan tersebut hidupnya sesilis?": {
                                                                                                                "Ya": Invertebrata['Kelas']["Echinodermata"]['Ordo'].get("Holothuroidea"),
                                                                                                                "Tidak": {
                                                                                                                    "Apakah hewan tersebut memiliki oral tetapi tidak ada anus?": {
                                                                                                                        "Ya": Invertebrata['Kelas']["Echinodermata"]['Ordo'].get("Ophiuroidea"),
                                                                                                                        "Tidak": "Klasifikasi salah!"
                                                                                                                    }
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }, "Tidak": "Data tidak ditemukan!"
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
