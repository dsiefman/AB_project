#!python2.7

import os
import numpy as np
import sys

# samp_file = '/home/daniel/AB_project/Sample_set/Dopamine_65/Dopamine_experiments/DNA_AT15azide/No_crosslinker/2017-06-22/Gel1_AT15azide/Gel1_2017-06-22/Gel1_2017-06-22.csv'
# TC = 'plastic'
def get_frames(samp_file, TC):

	# Open samp_folder and extract data split into frames and get y_axis for each

	# Open .csv file, load into array
	try:
		sys.stdout.write("READING CSV FILE...") # using sys instead of print to avoid newline
		csv_data = np.genfromtxt(samp_file, delimiter=',')
		# Delete first 64 cols,  only wavelengths 950 - 1400nm are included
		csv_data = np.delete(csv_data, range(64), 1)
		print(" COMPLETE")
	except IOError as e:
		print(" FATAL ERROR!!")
		print("\tInput .csv file not found")
		print("\tCheck existence of \n")
		print(samp_file)
		print(" ")
		sys.exit()


	frame_size = 513   # number of lines per frame
	num_frames = int(csv_data.shape[0]/frame_size) # num lines in file/frame_size

	print("\t%i FRAMES FOUND" % num_frames)

	# Plastic data for Transport Correction (TC)
	TC_plastic_string = '-0.003012730052939	-0.004865715025805	0.003199289290213	-0.003705156860417	-0.000512391006824	0.02266456822417	-0.003241486208513	0.000566745964349	0.001786703003706	0.00171430957642	-0.001481674497086	-0.003426786634772	0.000543042111228	-3.26471533700332E-05	0.002058833305659	-0.007464940137266	0.006778695694233	0.003750595953289	0.003778301320461	0.002634401484026	0.001855604525532	0.00684461386514	0.009469275469897	0.011381835397898	0.005728730031809	0.009572548322247	0.014499934829519	0.010390542511804	0.018079802916852	0.018809377505099	0.023599718368437	0.021218763841429	0.021779925452114	0.025567152352263	0.027939153855505	0.029444095336053	0.034161711830146	0.030651506466368	0.037563555921513	0.039706176202147	0.042930993068054	0.042609484214652	0.048624003112616	0.043441976742673	0.04563698608351	0.04719091824797	0.047898459113857	0.052519538052816	0.054295322289451	0.050002722099184	0.052550217355423	0.058074702405523	0.058484448965985	0.060680027961459	0.061488283865354	0.061632041203192	0.068549302349225	0.062258303016051	0.062268965173703	0.060676809019603	0.06264458844973	0.067533493933004	0.066137197088974	0.067319335895122	0.071111398502666	0.064367354576378	0.070181989054384	0.067763365509848	0.075962270081245	0.071568459172535	0.077183861401199	0.07389493309843	0.070191176341466	0.075185005400458	0.079712103871002	0.078639219042743	0.080645507213443	0.07593627713244	0.080426623649774	0.076826273470446	0.078548122558767	0.080405873515972	0.084917309644637	0.081938601403204	0.090161421009481	0.08973556813381	0.094101808444615	0.088148630744482	0.086266299043821	0.096658509779811	0.093994417898312	0.095257648246942	0.095510668845473	0.098629083514695	0.096584952401085	0.095208272049703	0.094692244115221	0.103271571839119	0.101891383129781	0.097189755483511	0.103882378092685	0.105626831026984	0.110346548168516	0.114530305497803	0.115015429433511	0.109830873469561	0.121426542004394	0.117313401652123	0.115201152162586	0.119958473114546	0.124436255036164	0.125414718813003	0.121700516397681	0.127246994160834	0.130360839738578	0.13214053042518	0.137632261538797	0.135133329146719	0.132564086844863	0.137821465054179	0.138075617869407	0.147464982363147	0.143370386221349	0.149461971143442	0.153005277284146	0.148111860562694	0.15436462161842	0.156952742776415	0.155873640009302	0.15298516272271	0.162547136443346	0.167661840598764	0.164843321772408	0.163210289091467	0.170159933398103	0.170911205491163	0.166996333348397	0.173323588175225	0.181268329452954	0.177890572371693	0.166509534782017	0.180988810330783	0.181354776931017	0.179374727500846	0.181000445854693	0.185134241665503	0.189209858720213	0.175694742312607	0.185335063911228	0.189876588403323	0.195783276833946	0.196041423726595	0.199352713080427	0.199733840500298	0.195079092813933	0.206151670207973	0.207912554241785	0.206206385349191	0.207179332835307	0.214259006021602	0.210966393297858	0.211200648604129	0.212354161087165	0.213452793775462	0.208990459289703	0.215508343020405	0.228178468115893	0.225506598278971	0.225745395568156	0.22999320909024	0.227894428584994	0.228087044155332	0.236807199889075	0.240197519223264	0.238891397733252	0.242060951260976	0.242750866939893	0.248858638442425	0.251873866762668	0.251846416968615	0.254649923961369	0.255120656609844	0.263849038299527	0.260515953665276	0.25730275833011	0.270939197121227	0.261761409349664	0.271544090149758	0.27419703615171	0.27700414041703	0.281888167703398	0.28093495799118	0.287561093891986	0.293982088025104	0.290203594751917	0.296755283096537	0.29334035820314	0.301757309122867	0.309764352496393	0.307012365148953	0.303642758194658	0.30963677690506	0.319692734954841	0.32195018179645	0.312188581464463	0.328999801641208	0.326005543815978	0.328803375194454	0.324125795996335	0.337644762715311	0.338615289610599	0.338010504843399	0.338425909713032	0.342857287633428	0.354849611292227	0.349772284980758	0.353927430370907	0.359373227791128	0.35244993001175	0.355216461339206	0.364375393813738	0.373991831498817	0.375310781262824	0.372079320104167	0.377414929568088	0.386143079874392	0.385410490601019	0.375408039710553	0.381397534113099	0.392512794814771	0.400541525950109	0.397377022066648	0.39947360220641	0.401272165579522	0.409177050174235	0.398344515267022	0.399928526912395	0.413435257206762	0.41651738059988	0.424412002170565	0.418542858077352	0.421351821386151	0.42473366042372	0.432252603509422	0.437278640312551	0.436365353316491	0.440637043052159	0.439010120019497	0.442609115381925	0.439983502618096	0.44200918465641	0.435376993004685	0.45167718267585	0.459636611541762	0.456045712808461	0.456695785741151	0.452856850756359	0.46105103530731	0.463502453100424	0.456368519903363	0.460590980633759	0.471375171395779	0.471763542025352	0.479936126557966	0.471237117861303	0.47370755760947	0.474355867860164	0.475934477946304	0.48006230101547	0.482010288939021	0.489586993717176	0.477288976885986	0.483547315183615	0.489405214698546	0.489202349577152	0.491886341554286	0.484871121688425	0.492450040457168	0.49369256040773	0.496148069625194	0.496004930823776	0.497182016154526	0.497253649611064	0.505906096925173	0.507090435031143	0.514916749595532	0.510069293931794	0.515751203646045	0.502984995718174	0.519991773432419	0.514671906945041	0.509129239132618	0.495228238089277	0.499081312467754	0.509859585176885	0.508459012072491	0.486258278875145	0.499016661499322	0.508579050561173	0.492219756523739	0.498732179797038	0.495675555402581	0.50370097601529	0.48541113986702	0.482635758808637	0.482455188526403	0.494387554312327	0.475619018094654	0.477901670778789	0.475408861978923	0.479983433454752	0.466272712174513	0.473732537713326	0.46796715931688	0.48032252494455	0.466998306185084	0.464366536438028	0.474823686433697	0.476819884111688	0.465751712778584	0.468239531889101	0.476415644413577	0.476660610199817	0.479660617581577	0.466252671263315	0.481173733821616	0.489630967410669	0.487422822211375	0.488123470316855	0.486795289156571	0.495700207196542	0.504994865984495	0.502712261699544	0.509134533457343	0.516992363720041	0.516626624676856	0.518116577352839	0.520056728607275	0.525566954589716	0.529085039530391	0.524929685643374	0.536492806903665	0.549738747711339	0.524198854165518	0.543180009357571	0.557314280979878	0.559237471871541	0.556594027719243	0.557040582473183	0.571753468517907	0.565276493549684	0.565073414718119	0.572298846892954	0.581674928053551	0.584367296811539	0.584539018316649	0.566372884631614	0.575679349597078	0.595857624449213	0.591629699380436	0.584251712866714	0.592839041618857	0.590247077908774	0.599549005869911	0.604649070130343	0.601139123197477	0.604850920631396	0.614839006583652	0.60312270158991	0.610897839226472	0.620896479647893	0.613494537544594	0.616015614580056	0.614091022771877	0.625732403086762	0.619528884797865	0.62701173433033	0.627705522856391	0.625825522524464	0.624440576208636	0.631884860168266	0.640271210684187	0.636926550237382	0.633514188263304	0.630972253612036	0.639504311923119	0.64960205670009	0.637436392059908	0.624656790616617	0.640126770048283	0.651998799801997	0.651089570665913	0.633995960716197	0.657672271059443	0.652842824928939	0.656581562527437	0.658497853957251	0.663855702773222	0.671518696437311	0.657009810377026	0.665116502977876	0.661984929180179	0.683261829460823	0.681147678243705	0.683801027360966	0.692606411176355	0.696486684745109	0.702268928176463	0.707219185875072	0.709889393926431	0.713095628795068	0.703122955112391	0.714233304051845	0.741523414042763	0.739769813285006	0.739974765391225	0.740700654578219	0.749245391082573	0.748379080180689	0.747469715166147	0.74188374341516	0.755452546131915	0.775254768678045	0.77346337814201	0.767732918535792	0.783810950730575	0.788104869803641	0.783870337467845	0.773498237329453	0.792434768814026	0.798998857496715	0.804787617409047	0.79480450268315	0.799214910791532	0.812591762907285	0.818692975776579	0.812242726545746	0.824718107213538	0.821792640367235	0.829830231425752	0.830643310977098	0.836759162817028	0.823318771810269	0.830717168664441	0.833270681992525	0.848224933403973	0.839049331919311	0.847458762764708	0.843527865908766	0.872969121172159	0.862775039975096	0.85664394696777	0.848578456192279	0.868444722146011	0.878533668626388	0.871830500589785	0.855237416450424	0.858737366354942	0.871723039390542	0.886923627685909	0.882929184443877	0.880247262346623	0.884279675548418	0.889440585719721	0.882723362397981	0.913180090765703	0.903709742813824	0.91374479739037	0.909267044754199	0.911817817093864	0.922668632570101	0.915046181362969	0.913873819751228	0.919606724953088	0.941948354543749	0.921620206739342	0.929030309650967	0.942126013442664	0.942268512322023	0.935909690262738	0.929501078696464	0.948332067210511	0.947379316531853	0.943482482263422	0.939579812341269	0.960631183585201	0.964685081086517	0.959639392588926	0.963324163009469	0.963520017192378	0.968289549320379	0.975654642882413	0.976090144955055	0.975247534107656	0.970763193866554	0.998899293429351	0.976105680264549	0.995131837588445	0.979201705973352	0.975112692568077	0.98181844025036	0.994420880615484	0.988037232366163	0.97902670367359	0.976031819678861	0.992053157629283	0.987628009486494	0.984444686444177	0.980559774650026	1.00366708412077	0.98536627503481	0.984730520800789	0.976011585505011	1.00114444829841	0.980710389677312	0.982403159808809	0.96891612496104	0.972831534263402	0.987478239009567	0.990403540896986	0.950711942251335	0.969893290455009	0.959510716220408	0.966124129446734	0.950085327971302	0.966809858867411	0.969423838705349	0.968875535434774	0.964051411764818	0.966567412509808	0.972808022834546	0.960227618017741	0.955522203229386	0.958132422414987	0.942341786817564	0.943671660261878	0.92482239315963	0.943347334517617	0.931799258717949	0.924375661233249	0.918143417659093	0.928587863690573	0.914719875004982	0.903629807797585	0.905054929508284	0.907815272972725	0.887490878867078	0.877729778630575	0.883504495197746	0.873063012511171	0.875014154567818	0.861523826980104	0.858044457793815	0.854800277269694	0.851046554411798	0.854180044431268	0.833331173952668	0.836060372434852	0.834024480718608	0.816343471210203	0.79954486069603	0.797950542251765	0.79792525449213	0.796036809563834	0.789608842369669	0.780013379781281	0.766526655312194	0.777942192307365	0.759944062775365	0.755477057147066	0.729425725315583	0.744974215008498	0.736227692924833	0.736719468541656	0.710705418843998	0.707398946317847	0.699613416900381	0.699809104735124	0.677246239268692	0.661505772635483	0.658876877696663	0.655358377940991	0.643655801808359	0.631047615823249	0.62244008046609	0.615072069615527	0.601151908186892	0.603871801922964	0.594540327574483	0.596400145658864	0.585186208646143	0.57787635545973	0.541622024921671	0.543366976241726	0.543309687024498	0.530341376499715	0.545224476387647	0.527916013032344	0.507372465784726	0.513300445176746	0.490872502427485	0.499554022810473	0.479400721940662	0.465664675911679	0.460454316729616	0.466921773455059	0.445318189143103	0.433995369650118	0.416839314779775	0.417985747253421	0.396760282208709	0.386499963966021	0.373190323148165	0.363870770237604	0.353463280179094	0.343633178715854	0.321693872345195	0.31264074327137	0.294156274298343	0.284658759406167	0.271144248574859	0.259284314715042	0.239689312163713	0.221089971688754	0.209197910490789	0.194526145377262	0.17815337094172	0.171652714437533	0.158949871085392	0.146258936214389	0.132836814639931	0.126726492560015	0.119769861300196	0.116569563920626	0.103406679454873	0.091670063686704	0.081775892083601	0.058619505173791	0.056067457817556	0.065295284022867'
	TC_plastic = [float(num) for num in TC_plastic_string.split('\t')[64:]]
	# Walk through csv matrix reading data based on frame_size
	frames = []
	for frame_num in range(0, csv_data.shape[0], frame_size):

		#y_axis_sum = csv_data.shape[1]
		#or row in csv_data[frame_num*frame_size:(fram_num+1)*fram_size]
		yaxis = sum(csv_data[frame_num:frame_num+frame_size, :])
		# Do transport correction with plastic or glass	or not at all
		if TC.lower() == "plastic":
			TC_spec = np.divide(yaxis, TC_plastic)
		elif TC.lower() == "glass":
			TC_spec = np.divide(yaxis, TC_glass)
		else:
			TC_spec = yaxis

		frames.append([yaxis, TC_spec])

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

	return x_axis, frames