#!python2.7

import numpy as np

def get_x_axis(grating):

	if grating == 75:
		x_axis = np.array([  949.4324341 ,   950.22170724,   951.01095951,   951.8001909 ,
						     952.58940141,   953.37859104,   954.16775976,   954.95690758,
						     955.74603448,   956.53514046,   957.32422551,   958.11328963,
						     958.90233279,   959.69135501,   960.48035626,   961.26933655,
						     962.05829586,   962.84723418,   963.63615151,   964.42504784,
						     965.21392317,   966.00277747,   966.79161076,   967.58042301,
						     968.36921422,   969.15798438,   969.94673349,   970.73546154,
						     971.52416851,   972.31285441,   973.10151921,   973.89016293,
						     974.67878554,   975.46738704,   976.25596742,   977.04452668,
						     977.8330648 ,   978.62158179,   979.41007762,   980.19855229,
						     980.9870058 ,   981.77543814,   982.5638493 ,   983.35223927,
						     984.14060804,   984.9289556 ,   985.71728196,   986.50558709,
						     987.293871  ,   988.08213367,   988.8703751 ,   989.65859528,
						     990.4467942 ,   991.23497185,   992.02312823,   992.81126332,
						     993.59937712,   994.38746963,   995.17554083,   995.96359072,
						     996.75161928,   997.53962652,   998.32761242,   999.11557697,
						     999.90352017,  1000.69144201,  1001.47934248,  1002.26722158,
						    1003.05507929,  1003.84291561,  1004.63073053,  1005.41852404,
						    1006.20629614,  1006.99404681,  1007.78177606,  1008.56948386,
						    1009.35717022,  1010.14483512,  1010.93247857,  1011.72010054,
						    1012.50770104,  1013.29528005,  1014.08283756,  1014.87037358,
						    1015.65788809,  1016.44538108,  1017.23285254,  1018.02030248,
						    1018.80773087,  1019.59513772,  1020.38252301,  1021.16988674,
						    1021.9572289 ,  1022.74454948,  1023.53184847,  1024.31912587,
						    1025.10638166,  1025.89361585,  1026.68082842,  1027.46801936,
						    1028.25518867,  1029.04233634,  1029.82946236,  1030.61656673,
						    1031.40364943,  1032.19071046,  1032.97774981,  1033.76476747,
						    1034.55176343,  1035.3387377 ,  1036.12569025,  1036.91262108,
						    1037.69953019,  1038.48641756,  1039.2732832 ,  1040.06012708,
						    1040.8469492 ,  1041.63374956,  1042.42052815,  1043.20728496,
						    1043.99401998,  1044.7807332 ,  1045.56742462,  1046.35409423,
						    1047.14074201,  1047.92736797,  1048.7139721 ,  1049.50055439,
						    1050.28711482,  1051.0736534 ,  1051.86017011,  1052.64666494,
						    1053.4331379 ,  1054.21958897,  1055.00601814,  1055.7924254 ,
						    1056.57881076,  1057.36517419,  1058.1515157 ,  1058.93783527,
						    1059.7241329 ,  1060.51040858,  1061.2966623 ,  1062.08289405,
						    1062.86910383,  1063.65529163,  1064.44145744,  1065.22760125,
						    1066.01372306,  1066.79982285,  1067.58590063,  1068.37195637,
						    1069.15799009,  1069.94400175,  1070.72999137,  1071.51595893,
						    1072.30190442,  1073.08782784,  1073.87372918,  1074.65960842,
						    1075.44546557,  1076.23130062,  1077.01711355,  1077.80290436,
						    1078.58867305,  1079.37441959,  1080.160144  ,  1080.94584625,
						    1081.73152635,  1082.51718428,  1083.30282003,  1084.0884336 ,
						    1084.87402499,  1085.65959417,  1086.44514115,  1087.23066592,
						    1088.01616847,  1088.80164879,  1089.58710687,  1090.37254271,
						    1091.1579563 ,  1091.94334763,  1092.7287167 ,  1093.51406349,
						    1094.299388  ,  1095.08469022,  1095.86997014,  1096.65522776,
						    1097.44046307,  1098.22567605,  1099.01086671,  1099.79603503,
						    1100.58118101,  1101.36630464,  1102.15140591,  1102.93648481,
						    1103.72154134,  1104.50657549,  1105.29158725,  1106.07657662,
						    1106.86154358,  1107.64648812,  1108.43141025,  1109.21630995,
						    1110.00118721,  1110.78604204,  1111.57087441,  1112.35568432,
						    1113.14047177,  1113.92523675,  1114.70997924,  1115.49469925,
						    1116.27939676,  1117.06407176,  1117.84872426,  1118.63335423,
						    1119.41796168,  1120.20254659,  1120.98710897,  1121.77164879,
						    1122.55616605,  1123.34066075,  1124.12513288,  1124.90958243,
						    1125.69400939,  1126.47841375,  1127.26279551,  1128.04715466,
						    1128.8314912 ,  1129.6158051 ,  1130.40009637,  1131.18436501,
						    1131.96861099,  1132.75283431,  1133.53703498,  1134.32121297,
						    1135.10536828,  1135.8895009 ,  1136.67361083,  1137.45769806,
						    1138.24176258,  1139.02580438,  1139.80982345,  1140.5938198 ,
						    1141.3777934 ,  1142.16174425,  1142.94567235,  1143.72957769,
						    1144.51346025,  1145.29732004,  1146.08115704,  1146.86497125,
						    1147.64876266,  1148.43253126,  1149.21627704,  1150.        ,
						    1150.78370013,  1151.56737742,  1152.35103186,  1153.13466345,
						    1153.91827217,  1154.70185803,  1155.48542101,  1156.2689611 ,
						    1157.05247831,  1157.83597261,  1158.619444  ,  1159.40289249,
						    1160.18631804,  1160.96972067,  1161.75310036,  1162.53645711,
						    1163.3197909 ,  1164.10310174,  1164.8863896 ,  1165.66965449,
						    1166.4528964 ,  1167.23611531,  1168.01931123,  1168.80248414,
						    1169.58563404,  1170.36876092,  1171.15186477,  1171.93494558,
						    1172.71800335,  1173.50103807,  1174.28404973,  1175.06703832,
						    1175.85000384,  1176.63294628,  1177.41586563,  1178.19876188,
						    1178.98163503,  1179.76448507,  1180.54731199,  1181.33011578,
						    1182.11289644,  1182.89565395,  1183.67838832,  1184.46109953,
						    1185.24378757,  1186.02645245,  1186.80909414,  1187.59171265,
						    1188.37430796,  1189.15688007,  1189.93942897,  1190.72195465,
						    1191.50445711,  1192.28693634,  1193.06939232,  1193.85182506,
						    1194.63423455,  1195.41662077,  1196.19898372,  1196.98132339,
						    1197.76363978,  1198.54593288,  1199.32820268,  1200.11044917,
						    1200.89267234,  1201.67487219,  1202.45704872,  1203.2392019 ,
						    1204.02133174,  1204.80343823,  1205.58552135,  1206.36758111,
						    1207.14961749,  1207.9316305 ,  1208.71362011,  1209.49558632,
						    1210.27752913,  1211.05944852,  1211.8413445 ,  1212.62321704,
						    1213.40506616,  1214.18689183,  1214.96869404,  1215.75047281,
						    1216.5322281 ,  1217.31395993,  1218.09566827,  1218.87735312,
						    1219.65901448,  1220.44065234,  1221.22226669,  1222.00385752,
						    1222.78542482,  1223.5669686 ,  1224.34848883,  1225.12998551,
						    1225.91145864,  1226.69290821,  1227.47433421,  1228.25573663,
						    1229.03711546,  1229.8184707 ,  1230.59980234,  1231.38111038,
						    1232.1623948 ,  1232.94365559,  1233.72489276,  1234.50610629,
						    1235.28729618,  1236.06846241,  1236.84960498,  1237.63072389,
						    1238.41181912,  1239.19289067,  1239.97393853,  1240.75496269,
						    1241.53596315,  1242.31693989,  1243.09789292,  1243.87882222,
						    1244.65972778,  1245.44060961,  1246.22146768,  1247.002302  ,
						    1247.78311255,  1248.56389934,  1249.34466234,  1250.12540155,
						    1250.90611698,  1251.6868086 ,  1252.46747641,  1253.24812041,
						    1254.02874058,  1254.80933692,  1255.58990942,  1256.37045808,
						    1257.15098288,  1257.93148383,  1258.7119609 ,  1259.4924141 ,
						    1260.27284341,  1261.05324884,  1261.83363036,  1262.61398798,
						    1263.39432169,  1264.17463148,  1264.95491734,  1265.73517926,
						    1266.51541725,  1267.29563128,  1268.07582135,  1268.85598746,
						    1269.6361296 ,  1270.41624776,  1271.19634193,  1271.97641211,
						    1272.75645828,  1273.53648045,  1274.31647859,  1275.09645272,
						    1275.87640281,  1276.65632886,  1277.43623087,  1278.21610883,
						    1278.99596272,  1279.77579254,  1280.55559829,  1281.33537995,
						    1282.11513753,  1282.894871  ,  1283.67458037,  1284.45426563,
						    1285.23392677,  1286.01356377,  1286.79317665,  1287.57276538,
						    1288.35232996,  1289.13187038,  1289.91138664,  1290.69087873,
						    1291.47034664,  1292.24979036,  1293.02920989,  1293.80860521,
						    1294.58797633,  1295.36732323,  1296.1466459 ,  1296.92594435,
						    1297.70521855,  1298.48446851,  1299.26369422,  1300.04289567,
						    1300.82207285,  1301.60122575,  1302.38035437,  1303.1594587 ,
						    1303.93853873,  1304.71759446,  1305.49662588,  1306.27563297,
						    1307.05461574,  1307.83357418,  1308.61250827,  1309.39141802,
						    1310.17030341,  1310.94916443,  1311.72800108,  1312.50681336,
						    1313.28560125,  1314.06436475,  1314.84310384,  1315.62181853,
						    1316.4005088 ,  1317.17917466,  1317.95781608,  1318.73643306,
						    1319.5150256 ,  1320.29359369,  1321.07213732,  1321.85065648,
						    1322.62915117,  1323.40762137,  1324.18606709,  1324.96448832,
						    1325.74288503,  1326.52125724,  1327.29960494,  1328.0779281 ,
						    1328.85622673,  1329.63450083,  1330.41275038,  1331.19097537,
						    1331.9691758 ,  1332.74735166,  1333.52550295,  1334.30362965,
						    1335.08173176,  1335.85980927,  1336.63786218,  1337.41589047,
						    1338.19389414,  1338.97187319,  1339.7498276 ,  1340.52775737,
						    1341.30566248,  1342.08354295,  1342.86139874,  1343.63922987,
						    1344.41703632,  1345.19481808,  1345.97257515,  1346.75030752,
						    1347.52801518,  1348.30569812,  1349.08335634,  1349.86098984,
						    1350.63859859,  1351.4161826 ,  1352.19374186,  1352.97127636,
						    1353.74878609,  1354.52627105,  1355.30373123,  1356.08116663,
						    1356.85857722,  1357.63596302,  1358.413324  ,  1359.19066016,
						    1359.96797151,  1360.74525802,  1361.52251969,  1362.29975651,
						    1363.07696848,  1363.85415559,  1364.63131783,  1365.4084552 ,
						    1366.18556768,  1366.96265528,  1367.73971797,  1368.51675577,
						    1369.29376865,  1370.07075661,  1370.84771964,  1371.62465774,
						    1372.40157091,  1373.17845912,  1373.95532238,  1374.73216067,
						    1375.508974  ,  1376.28576234,  1377.06252571,  1377.83926408,
						    1378.61597745,  1379.39266582,  1380.16932918,  1380.94596751,
						    1381.72258081,  1382.49916909,  1383.27573231,  1384.05227049,
						    1384.82878362,  1385.60527167,  1386.38173466,  1387.15817257,
						    1387.93458539,  1388.71097312,  1389.48733575,  1390.26367328,
						    1391.03998568,  1391.81627297,  1392.59253513,  1393.36877215,
						    1394.14498403,  1394.92117075,  1395.69733232,  1396.47346872,
						    1397.24957996,  1398.02566601,  1398.80172687,  1399.57776254])

	elif grating == 600:
		x_axis = np.array([961.178691,961.2696943,961.3606937,961.451689,961.5426803,961.6336675,961.7246508,961.815630,961.9066051,961.9975763,962.0885433,962.1795064,962.2704654,962.3614204,962.4523713,962.5433182,962.6342611,962.7251999,962.8161347,962.9070654,962.9979921,963.0889148,963.1798334,963.2707479,963.3616585,963.4525649,963.5434673,963.6343657,963.725260,963.8161503,963.9070365,963.9979187,964.0887968,964.1796708,964.2705408,964.3614068,964.4522686,964.5431265,964.6339802,964.7248299,964.8156756,964.9065172,964.9973547,965.0881882,965.1790176,965.2698429,965.3606642,965.4514814,965.5422945,965.6331036,965.7239086,965.8147095,965.9055064,965.9962992,966.0870879,966.1778725,966.2686531,966.3594296,966.450202,966.5409703,966.6317346,966.7224948,966.8132509,966.9040029,966.9947509,967.0854948,967.1762346,967.2669703,967.3577019,967.4484294,967.5391529,967.6298722,967.7205875,967.8112987,967.9020058,967.9927088,968.0834078,968.1741026,968.2647933,968.355480,968.4461625,968.536841,968.6275153,968.7181856,968.8088518,968.8995139,968.9901718,969.0808257,969.1714755,969.2621212,969.3527627,969.4434002,969.5340336,969.6246628,969.715288,969.805909,969.896526,969.9871388,970.0777475,970.1683522,970.2589527,970.3495491,970.4401413,970.5307295,970.6213136,970.7118935,970.8024694,970.8930411,970.9836087,971.0741721,971.1647315,971.2552867,971.3458379,971.4363849,971.5269277,971.6174665,971.7080011,971.7985316,971.889058,971.9795803,972.0700984,972.1606124,972.2511223,972.341628,972.4321297,972.5226271,972.6131205,972.7036097,972.7940948,972.8845758,972.9750526,973.0655253,973.1559938,973.2464582,973.3369185,973.4273746,973.5178266,973.6082745,973.6987182,973.7891577,973.8795932,973.9700245,974.0604516,974.1508746,974.2412934,974.3317081,974.4221187,974.5125251,974.6029273,974.6933254,974.7837194,974.8741092,974.9644948,975.0548763,975.1452536,975.2356268,975.3259958,975.4163607,975.5067214,975.597078,975.6874304,975.7777786,975.8681227,975.9584626,976.0487983,976.1391299,976.2294573,976.3197806,976.4100997,976.5004146,976.5907253,976.6810319,976.7713343,976.8616326,976.9519266,977.0422165,977.1325023,977.2227838,977.3130612,977.4033344,977.4936034,977.5838683,977.674129,977.7643855,977.8546378,977.9448859,978.0351299,978.1253697,978.2156053,978.3058367,978.3960639,978.486287,978.5765058,978.6667205,978.756931,978.8471373,978.9373394,979.0275373,979.117731,979.2079206,979.2981059,979.3882871,979.478464,979.5686368,979.6588054,979.7489697,979.8391299,979.9292859,980.0194377,980.1095852,980.1997286,980.2898678,980.3800028,980.4701336,980.5602601,980.6503825,980.7405007,980.8306146,980.9207244,981.0108299,981.1009313,981.1910284,981.2811213,981.371210,981.4612945,981.5513748,981.6414509,981.7315227,981.8215904,981.9116538,982.001713,982.091768,982.1818188,982.2718653,982.3619077,982.4519458,982.5419797,982.6320094,982.7220348,982.8120561,982.9020731,982.9920858,983.0820944,983.1720987,983.2620988,983.3520947,983.4420863,983.5320738,983.6220569,983.7120359,983.8020106,983.8919811,983.9819474,984.0719094,984.1618672,984.2518207,984.341770,984.4317151,984.5216559,984.6115925,984.7015249,984.791453,984.8813768,984.9712965,985.0612119,985.151123,985.2410299,985.3309326,985.420831,985.5107251,985.600615,985.6905007,985.7803821,985.8702592,985.9601322,986.0500008,986.1398652,986.2297254,986.3195813,986.4094329,986.4992803,986.5891234,986.6789623,986.7687969,986.8586272,986.9484533,987.0382752,987.1280927,987.217906,987.3077151,987.3975198,987.4873204,987.5771166,987.6669086,987.7566963,987.8464798,987.9362589,988.0260338,988.1158045,988.2055708,988.2953329,988.3850908,988.4748443,988.5645936,988.6543386,988.7440793,988.8338157,988.9235479,989.0132758,989.1029994,989.1927187,989.2824338,989.3721446,989.4618511,989.5515533,989.6412512,989.7309448,989.8206342,989.9103192,990,990.0896765,990.1793487,990.2690166,990.3586802,990.4483396,990.5379946,990.6276453,990.7172918,990.8069339,990.8965718,990.9862054,991.0758347,991.1654596,991.2550803,991.3446967,991.4343088,991.5239165,991.613520,991.7031192,991.7927141,991.8823046,991.9718909,992.0614729,992.1510505,992.2406239,992.3301929,992.4197576,992.509318,992.5988742,992.688426,992.7779735,992.8675166,992.9570555,993.0465901,993.1361203,993.2256462,993.3151678,993.4046851,993.4941981,993.5837067,993.6732111,993.7627111,993.8522068,993.9416982,994.0311852,994.1206679,994.2101463,994.2996204,994.3890902,994.4785556,994.5680167,994.6574735,994.7469259,994.836374,994.9258178,995.0152573,995.1046924,995.1941232,995.2835497,995.3729718,995.4623896,995.551803,995.6412121,995.7306169,995.8200174,995.9094135,995.9988052,996.0881927,996.1775757,996.2669545,996.3563289,996.4456989,996.5350647,996.624426,996.713783,996.8031357,996.8924841,996.981828,997.0711677,997.1605029,997.2498339,997.3391605,997.4284827,997.5178006,997.6071141,997.6964233,997.7857281,997.8750285,997.9643247,998.0536164,998.1429038,998.2321868,998.3214655,998.4107398,998.5000098,998.5892753,998.6785366,998.7677934,998.8570459,998.9462941,999.0355378,999.1247772,999.2140123,999.3032429,999.3924692,999.4816912,999.5709087,999.6601219,999.7493307,999.8385352,999.9277352,1000.016931,1000.106122,1000.195309,1000.284492,1000.37367,1000.462844,1000.552013,1000.641178,1000.730339,1000.819495,1000.908647,1000.997795,1001.086938,1001.176077,1001.265211,1001.354341,1001.443467,1001.532588,1001.621705,1001.710817,1001.799925,1001.889029,1001.978128,1002.067223,1002.156313,1002.24540,1002.334481,1002.423559,1002.512631,1002.60170,1002.690764,1002.779824,1002.868879,1002.95793,1003.046977,1003.136019,1003.225056,1003.31409,1003.403119,1003.492143,1003.581163,1003.670179,1003.75919,1003.848197,1003.93720,1004.026198,1004.115191,1004.204181,1004.293166,1004.382146,1004.471122,1004.560094,1004.649061,1004.738024,1004.826982,1004.915936,1005.004885,1005.093831,1005.182771,1005.271707,1005.360639,1005.449567,1005.53849,1005.627408,1005.716323,1005.805232,1005.894138,1005.983039,1006.071935,1006.160827,1006.249715,1006.338598,1006.427477,1006.516351,1006.605221,1006.694086,1006.782947,1006.871804,1006.960656,1007.049504,1007.138347,1007.227186,1007.316021,1007.404851,1007.493676,1007.582497,1007.671314,1007.760126,1007.848934,1007.937737,1008.026536,1008.115331,1008.204121,1008.292906,1008.381687,1008.470464,1008.559236,1008.648004,1008.736767,1008.825526,1008.914281,1009.003031,1009.091776,1009.180518,1009.269254,1009.357986,1009.446714,1009.535437,1009.624156,1009.712871,1009.80158,1009.890286,1009.978987,1010.067683,1010.156376,1010.245063,1010.333746,1010.422425,1010.511099,1010.599769,1010.688434,1010.777095,1010.865751,1010.954403,1011.043051,1011.131694,1011.220332,1011.308966,1011.397596,1011.486221,1011.574842,1011.663458,1011.752069,1011.840677,1011.929279,1012.017878,1012.106471,1012.195061,1012.283645,1012.372226,1012.460802,1012.549373,1012.63794,1012.726502,1012.81506,1012.903614,1012.992163,1013.080707,1013.169247,1013.257782,1013.346313,1013.43484,1013.523362,1013.61188,1013.700393,1013.788901,1013.877405,1013.965905,1014.05440,1014.142891,1014.231377,1014.319858,1014.408335,1014.496808,1014.585276,1014.67374,1014.762199,1014.850653,1014.939104,1015.027549,1015.11599,1015.204427,1015.292859,1015.381287,1015.46971,1015.558128,1015.646542,1015.734952,1015.823357,1015.911758,1016.000154,1016.088545,1016.176932,1016.265315,1016.353693,1016.442066,1016.530435,1016.61880,1016.70716,1016.795515,1016.883866,1016.972213,1017.060555,1017.148892,1017.237225,1017.325553,1017.413877,1017.502196,1017.590511,1017.678821,1017.767127,1017.855428,1017.943725,1018.032017,1018.120305,1018.208588,1018.296866,1018.38514,1018.47341])

	else:

		print('ERROR: REQUESTED GRATING %i NOT RECOGNIZED', grating)
		print('ONLY %i OR %i CURRENTLY ALLOWED' % 75, 600)

	return(x_axis)