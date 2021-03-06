#!python2.7

import os
import numpy as np
import sys, time
import lmfit   # module to do Lorentz fitting
import matplotlib.pyplot as plt
import re, sys

# Custom module
import xData


##################################################################


def completed(t):

	# Function to print time since t

	print('\tCOMPLETED IN %i SECONDS' % int(time.time() - t))


##################################################################


def get_frames(samp_file, TC='plastic', smooth_flag=True, grating=600):


	'''
	Read samp_file and extract y-axis data for each frame
	Smooth the data and perform transport correction if requested

	INPUTS:
		-samp_file [string]: Name of .csv to read data from
		-TC [string]: Requested transport correction. Only plastic
					  has so far been programmed. Default is plastic.
		-smooth_flag [bool]: Option to smooth intensity data.
							 Default is true, or to smooth
		-grating [integer]: grating type, sets x-axis bins. Default is 600

	OUTPUTS:	
		-x_axis [numpy vector]: x-axis (wavelength) values corresponding to intensity data
		-frames [list of numpy arrays]: List where each element is a frame's intensity data
	'''

	t = time.time()   # start timer

	print("\tREADING CSV FILE...")
	# sys.stdout.write("READING CSV FILE...") # using sys instead of print to avoid newline
	# Open .csv file, load into array
	try:
		csv_data = np.genfromtxt(samp_file, delimiter=',')
		# Delete first 64 cols,  only wavelengths afger 950nm are included
		if grating == 75:
			csv_data = np.delete(csv_data, range(64), 1)
	except IOError as e:
		print(" FATAL ERROR!!")
		print("\tInput .csv file not found")
		print("\tCheck existence of \n")
		print(samp_file)
		print(" ")
		sys.exit()

	if TC:
		print("\t\tTRANSPORT CORRECTION DONE WITH %s DATA" % TC)

		# Error if option other than plastic is given
		if TC.lower() != 'plastic':
			print('\n\tERROR: TRANSPORT CORRECTION %s NOT RECOGNIZED' % TC)
			print('\tONLY plastic CURRENTLY ALLOWED')
			raise

	else:
		print("\t\tNO TRANSPORT CORRECTION PERFORMED")

	frame_size = 513   # number of lines per frame
	num_frames = int(csv_data.shape[0]/frame_size) # num lines in file/frame_size

	print("\t\t%i FRAMES FOUND" % num_frames)

	# Walk through csv matrix reading data based on frame_size
	frames = []
	for frame_num in range(0, csv_data.shape[0], frame_size):

		#y_axis_sum = csv_data.shape[1]
		#or row in csv_data[frame_num*frame_size:(fram_num+1)*fram_size]
		yaxis = sum(csv_data[frame_num:frame_num+frame_size, :])
		# Do transport correction with plastic or glass	or not at all
		if not TC:
			pass
		elif TC.lower() == "plastic":
			# Plastic data for Transport Correction (TC)
			TC_plastic_string = '-0.003012730052939	-0.004865715025805	0.003199289290213	-0.003705156860417	-0.000512391006824	0.02266456822417	-0.003241486208513	0.000566745964349	0.001786703003706	0.00171430957642	-0.001481674497086	-0.003426786634772	0.000543042111228	-3.26471533700332E-05	0.002058833305659	-0.007464940137266	0.006778695694233	0.003750595953289	0.003778301320461	0.002634401484026	0.001855604525532	0.00684461386514	0.009469275469897	0.011381835397898	0.005728730031809	0.009572548322247	0.014499934829519	0.010390542511804	0.018079802916852	0.018809377505099	0.023599718368437	0.021218763841429	0.021779925452114	0.025567152352263	0.027939153855505	0.029444095336053	0.034161711830146	0.030651506466368	0.037563555921513	0.039706176202147	0.042930993068054	0.042609484214652	0.048624003112616	0.043441976742673	0.04563698608351	0.04719091824797	0.047898459113857	0.052519538052816	0.054295322289451	0.050002722099184	0.052550217355423	0.058074702405523	0.058484448965985	0.060680027961459	0.061488283865354	0.061632041203192	0.068549302349225	0.062258303016051	0.062268965173703	0.060676809019603	0.06264458844973	0.067533493933004	0.066137197088974	0.067319335895122	0.071111398502666	0.064367354576378	0.070181989054384	0.067763365509848	0.075962270081245	0.071568459172535	0.077183861401199	0.07389493309843	0.070191176341466	0.075185005400458	0.079712103871002	0.078639219042743	0.080645507213443	0.07593627713244	0.080426623649774	0.076826273470446	0.078548122558767	0.080405873515972	0.084917309644637	0.081938601403204	0.090161421009481	0.08973556813381	0.094101808444615	0.088148630744482	0.086266299043821	0.096658509779811	0.093994417898312	0.095257648246942	0.095510668845473	0.098629083514695	0.096584952401085	0.095208272049703	0.094692244115221	0.103271571839119	0.101891383129781	0.097189755483511	0.103882378092685	0.105626831026984	0.110346548168516	0.114530305497803	0.115015429433511	0.109830873469561	0.121426542004394	0.117313401652123	0.115201152162586	0.119958473114546	0.124436255036164	0.125414718813003	0.121700516397681	0.127246994160834	0.130360839738578	0.13214053042518	0.137632261538797	0.135133329146719	0.132564086844863	0.137821465054179	0.138075617869407	0.147464982363147	0.143370386221349	0.149461971143442	0.153005277284146	0.148111860562694	0.15436462161842	0.156952742776415	0.155873640009302	0.15298516272271	0.162547136443346	0.167661840598764	0.164843321772408	0.163210289091467	0.170159933398103	0.170911205491163	0.166996333348397	0.173323588175225	0.181268329452954	0.177890572371693	0.166509534782017	0.180988810330783	0.181354776931017	0.179374727500846	0.181000445854693	0.185134241665503	0.189209858720213	0.175694742312607	0.185335063911228	0.189876588403323	0.195783276833946	0.196041423726595	0.199352713080427	0.199733840500298	0.195079092813933	0.206151670207973	0.207912554241785	0.206206385349191	0.207179332835307	0.214259006021602	0.210966393297858	0.211200648604129	0.212354161087165	0.213452793775462	0.208990459289703	0.215508343020405	0.228178468115893	0.225506598278971	0.225745395568156	0.22999320909024	0.227894428584994	0.228087044155332	0.236807199889075	0.240197519223264	0.238891397733252	0.242060951260976	0.242750866939893	0.248858638442425	0.251873866762668	0.251846416968615	0.254649923961369	0.255120656609844	0.263849038299527	0.260515953665276	0.25730275833011	0.270939197121227	0.261761409349664	0.271544090149758	0.27419703615171	0.27700414041703	0.281888167703398	0.28093495799118	0.287561093891986	0.293982088025104	0.290203594751917	0.296755283096537	0.29334035820314	0.301757309122867	0.309764352496393	0.307012365148953	0.303642758194658	0.30963677690506	0.319692734954841	0.32195018179645	0.312188581464463	0.328999801641208	0.326005543815978	0.328803375194454	0.324125795996335	0.337644762715311	0.338615289610599	0.338010504843399	0.338425909713032	0.342857287633428	0.354849611292227	0.349772284980758	0.353927430370907	0.359373227791128	0.35244993001175	0.355216461339206	0.364375393813738	0.373991831498817	0.375310781262824	0.372079320104167	0.377414929568088	0.386143079874392	0.385410490601019	0.375408039710553	0.381397534113099	0.392512794814771	0.400541525950109	0.397377022066648	0.39947360220641	0.401272165579522	0.409177050174235	0.398344515267022	0.399928526912395	0.413435257206762	0.41651738059988	0.424412002170565	0.418542858077352	0.421351821386151	0.42473366042372	0.432252603509422	0.437278640312551	0.436365353316491	0.440637043052159	0.439010120019497	0.442609115381925	0.439983502618096	0.44200918465641	0.435376993004685	0.45167718267585	0.459636611541762	0.456045712808461	0.456695785741151	0.452856850756359	0.46105103530731	0.463502453100424	0.456368519903363	0.460590980633759	0.471375171395779	0.471763542025352	0.479936126557966	0.471237117861303	0.47370755760947	0.474355867860164	0.475934477946304	0.48006230101547	0.482010288939021	0.489586993717176	0.477288976885986	0.483547315183615	0.489405214698546	0.489202349577152	0.491886341554286	0.484871121688425	0.492450040457168	0.49369256040773	0.496148069625194	0.496004930823776	0.497182016154526	0.497253649611064	0.505906096925173	0.507090435031143	0.514916749595532	0.510069293931794	0.515751203646045	0.502984995718174	0.519991773432419	0.514671906945041	0.509129239132618	0.495228238089277	0.499081312467754	0.509859585176885	0.508459012072491	0.486258278875145	0.499016661499322	0.508579050561173	0.492219756523739	0.498732179797038	0.495675555402581	0.50370097601529	0.48541113986702	0.482635758808637	0.482455188526403	0.494387554312327	0.475619018094654	0.477901670778789	0.475408861978923	0.479983433454752	0.466272712174513	0.473732537713326	0.46796715931688	0.48032252494455	0.466998306185084	0.464366536438028	0.474823686433697	0.476819884111688	0.465751712778584	0.468239531889101	0.476415644413577	0.476660610199817	0.479660617581577	0.466252671263315	0.481173733821616	0.489630967410669	0.487422822211375	0.488123470316855	0.486795289156571	0.495700207196542	0.504994865984495	0.502712261699544	0.509134533457343	0.516992363720041	0.516626624676856	0.518116577352839	0.520056728607275	0.525566954589716	0.529085039530391	0.524929685643374	0.536492806903665	0.549738747711339	0.524198854165518	0.543180009357571	0.557314280979878	0.559237471871541	0.556594027719243	0.557040582473183	0.571753468517907	0.565276493549684	0.565073414718119	0.572298846892954	0.581674928053551	0.584367296811539	0.584539018316649	0.566372884631614	0.575679349597078	0.595857624449213	0.591629699380436	0.584251712866714	0.592839041618857	0.590247077908774	0.599549005869911	0.604649070130343	0.601139123197477	0.604850920631396	0.614839006583652	0.60312270158991	0.610897839226472	0.620896479647893	0.613494537544594	0.616015614580056	0.614091022771877	0.625732403086762	0.619528884797865	0.62701173433033	0.627705522856391	0.625825522524464	0.624440576208636	0.631884860168266	0.640271210684187	0.636926550237382	0.633514188263304	0.630972253612036	0.639504311923119	0.64960205670009	0.637436392059908	0.624656790616617	0.640126770048283	0.651998799801997	0.651089570665913	0.633995960716197	0.657672271059443	0.652842824928939	0.656581562527437	0.658497853957251	0.663855702773222	0.671518696437311	0.657009810377026	0.665116502977876	0.661984929180179	0.683261829460823	0.681147678243705	0.683801027360966	0.692606411176355	0.696486684745109	0.702268928176463	0.707219185875072	0.709889393926431	0.713095628795068	0.703122955112391	0.714233304051845	0.741523414042763	0.739769813285006	0.739974765391225	0.740700654578219	0.749245391082573	0.748379080180689	0.747469715166147	0.74188374341516	0.755452546131915	0.775254768678045	0.77346337814201	0.767732918535792	0.783810950730575	0.788104869803641	0.783870337467845	0.773498237329453	0.792434768814026	0.798998857496715	0.804787617409047	0.79480450268315	0.799214910791532	0.812591762907285	0.818692975776579	0.812242726545746	0.824718107213538	0.821792640367235	0.829830231425752	0.830643310977098	0.836759162817028	0.823318771810269	0.830717168664441	0.833270681992525	0.848224933403973	0.839049331919311	0.847458762764708	0.843527865908766	0.872969121172159	0.862775039975096	0.85664394696777	0.848578456192279	0.868444722146011	0.878533668626388	0.871830500589785	0.855237416450424	0.858737366354942	0.871723039390542	0.886923627685909	0.882929184443877	0.880247262346623	0.884279675548418	0.889440585719721	0.882723362397981	0.913180090765703	0.903709742813824	0.91374479739037	0.909267044754199	0.911817817093864	0.922668632570101	0.915046181362969	0.913873819751228	0.919606724953088	0.941948354543749	0.921620206739342	0.929030309650967	0.942126013442664	0.942268512322023	0.935909690262738	0.929501078696464	0.948332067210511	0.947379316531853	0.943482482263422	0.939579812341269	0.960631183585201	0.964685081086517	0.959639392588926	0.963324163009469	0.963520017192378	0.968289549320379	0.975654642882413	0.976090144955055	0.975247534107656	0.970763193866554	0.998899293429351	0.976105680264549	0.995131837588445	0.979201705973352	0.975112692568077	0.98181844025036	0.994420880615484	0.988037232366163	0.97902670367359	0.976031819678861	0.992053157629283	0.987628009486494	0.984444686444177	0.980559774650026	1.00366708412077	0.98536627503481	0.984730520800789	0.976011585505011	1.00114444829841	0.980710389677312	0.982403159808809	0.96891612496104	0.972831534263402	0.987478239009567	0.990403540896986	0.950711942251335	0.969893290455009	0.959510716220408	0.966124129446734	0.950085327971302	0.966809858867411	0.969423838705349	0.968875535434774	0.964051411764818	0.966567412509808	0.972808022834546	0.960227618017741	0.955522203229386	0.958132422414987	0.942341786817564	0.943671660261878	0.92482239315963	0.943347334517617	0.931799258717949	0.924375661233249	0.918143417659093	0.928587863690573	0.914719875004982	0.903629807797585	0.905054929508284	0.907815272972725	0.887490878867078	0.877729778630575	0.883504495197746	0.873063012511171	0.875014154567818	0.861523826980104	0.858044457793815	0.854800277269694	0.851046554411798	0.854180044431268	0.833331173952668	0.836060372434852	0.834024480718608	0.816343471210203	0.79954486069603	0.797950542251765	0.79792525449213	0.796036809563834	0.789608842369669	0.780013379781281	0.766526655312194	0.777942192307365	0.759944062775365	0.755477057147066	0.729425725315583	0.744974215008498	0.736227692924833	0.736719468541656	0.710705418843998	0.707398946317847	0.699613416900381	0.699809104735124	0.677246239268692	0.661505772635483	0.658876877696663	0.655358377940991	0.643655801808359	0.631047615823249	0.62244008046609	0.615072069615527	0.601151908186892	0.603871801922964	0.594540327574483	0.596400145658864	0.585186208646143	0.57787635545973	0.541622024921671	0.543366976241726	0.543309687024498	0.530341376499715	0.545224476387647	0.527916013032344	0.507372465784726	0.513300445176746	0.490872502427485	0.499554022810473	0.479400721940662	0.465664675911679	0.460454316729616	0.466921773455059	0.445318189143103	0.433995369650118	0.416839314779775	0.417985747253421	0.396760282208709	0.386499963966021	0.373190323148165	0.363870770237604	0.353463280179094	0.343633178715854	0.321693872345195	0.31264074327137	0.294156274298343	0.284658759406167	0.271144248574859	0.259284314715042	0.239689312163713	0.221089971688754	0.209197910490789	0.194526145377262	0.17815337094172	0.171652714437533	0.158949871085392	0.146258936214389	0.132836814639931	0.126726492560015	0.119769861300196	0.116569563920626	0.103406679454873	0.091670063686704	0.081775892083601	0.058619505173791	0.056067457817556	0.065295284022867'
			TC_plastic = [float(num) for num in TC_plastic_string.split('\t')]
			if grating == 75:
				del TC_plastic[0:64]
			yaxis = np.divide(yaxis, TC_plastic)
		elif TC.lower() == "glass":
			yaxis = np.divide(yaxis, TC_glass)

		# Smooth the yaxis and TC_spec data, smoothing window of 5 data points
		if smooth_flag:
			yaxis = smooth(yaxis, 5)

		frames.append(yaxis)

	x_axis = xData.get_x_axis(grating)

	completed(t)

	return x_axis, frames


##################################################################


def smooth(a,WSZ):

    ''' 
    Replicate smooth function in MATLAB
    Taken from 
    https://stackoverflow.com/questions/40443020/matlabs-smooth-implementation-n-point-moving-average-in-numpy-python
    
    INPUTS:
    	-a: NumPy 1-D array containing the data to be smoothed
    	-WSZ: smoothing window size needs, which must be odd number,
    		 as in the original MATLAB implementation

	OUTPUTS:
		- smoother numpy vector
    '''

    out0 = np.convolve(a,np.ones(WSZ,dtype=int),'valid')/WSZ    
    r = np.arange(1,WSZ-1,2)
    start = np.cumsum(a[:WSZ-1])[::2]/r
    stop = (np.cumsum(a[:-WSZ:-1])[::2]/r)[::-1]
    return np.concatenate((  start , out0, stop  ))


##################################################################


def FindPeak(x_axis, frames, peak):


	'''
	Find maximums in the y-data for specific photopeaks from smoothed data
	Return the maximums of the peak for each frame
	# Indices where peak ranges are in data
	# For 1025nm-1070nm (7,5)
	# peak1 = [78, 167]   # 1010.932479 nm & 1080.945846 nm
	# # For 1110-1180nm (7,6)
	# peak2 = [190, 358]   # 1099.010867 nm & 1230.599802 nm
	# # For 1250nm-1325nm (9,5)
	# peak3 = [384, 480]   # 1250.906117 nm & 1325.742885 nm
	# peaks = [peak1, peak2, peak3]
	peaks = [[320, 460]]  #986.4993 1002.5 nm (6,5 peak)

	INPUTS:
		-x_axis [numpy array]: x-axis data for plots (wavelengths in nm)
		-frames [list of numpy arrays]: y-axis data (intensity) for individual frames
		-peak [list]: Upper (peak[0]) and lower (peak[1]) indices that mark
				      range of interest for photopeak

	OUTPUTS:
        -center [float]: Center of photopeak (wavelength)
        -height [float]: Height of photopeak (intensity)
    '''

	# Get index where max is in y-axis data
	iMax = np.argmax(frame[peak[0]:peak[1]]) 

	# Use index to get y_max and the x_data that it corresponds to
	center = x_axis[iMax]
	height = frame[iMax]

	return center, height


##################################################################


def LorentzFindPeak(x, y):


    '''
     Fit a single peak to a Lorentzian distribution and
     return distribution paramters

    INPUTS:
        -x [numpy array]: independent variable for fitting, wavelenght in nm
        -y [numpy array]:: Dependent variable, intensities corresponding to wavelengths

    OUTPUTS:
        -center [list]: Center of Lorentzian and 1sigma (absolute)
        -height [list]: Height of Lorentzian and 1sigma (absolute)
        -fwhm [list]: Full-width @ half max of Lorentzian and 1sigma (absolute)
    '''

    t = time.time()

    # Fits work better as Energy instead of wavelength
    # convert to E, must flip vector
    x = 1240/x[::-1]  # convert from nm to eV
    y = y[::-1]

    # Do Lorentzian fit with lmfit module
    gmodel = lmfit.models.LorentzianModel()
    pars = gmodel.guess(y, x=x)  # Guess the parameters for the distribution (amplitude, width)
    result = gmodel.fit(y, pars, x=x)  # Do the fit with the guessed parametres

    # plt.plot(x, y,         'bo')    
    # plt.plot(x, result.init_fit, 'k--')
    # plt.plot(x, result.best_fit, 'r-')
    # plt.show()
    # plt.close()

    fit_report = result.fit_report()
    # Extract data with regular expressions
    # First make regex to extract numbers after string
    numberRegEx = ':\W+([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)\W+\+\/-\W+([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)'   # Match any number

    # Then match regex
    center_data = re.search('center'+ numberRegEx, fit_report)
    height_data = re.search('height'+ numberRegEx, fit_report)
    fwhm_data = re.search('fwhm'+ numberRegEx, fit_report)

    # Get the value and its unc (1 absolute std), convert to float
    centers = [float(x) for x in center_data.groups()]
    heights = [float(x) for x in height_data.groups()]
    fwhms = [float(x) for x in fwhm_data.groups()]

    # Correct center data back to wavelength
    centers[0] = 1240/centers[0]
    centers[1] = 1240*centers[1]  # error propagation for exponent: x^-1 = x

    return centers, heights, fwhms

###############################################################################

def fit_samp_file(x, frames, grating=600):

	
	# Indices where peak ranges are in data
	# Options if in future we want multiple peaks
	# For 1025nm-1070nm (7,5)
	# peak1 = [78, 167]   # 1010.932479 nm & 1080.945846 nm
	# # For 1110-1180nm (7,6)
	# peak2 = [190, 358]   # 1099.010867 nm & 1230.599802 nm
	# # For 1250nm-1325nm (9,5)
	# peak3 = [384, 480]   # 1250.906117 nm & 1325.742885 nm
	# peaks = [peak1, peak2, peak3]

	# For 600 grating at 950-1050nm (6,5 peak)
	if grating == 600:
		peaks = [[320, 460]]
	# For 75 grating at 950-1050nm (6,5 peak)
	elif grating == 75:
		peaks = [[0, 128]]
	else:
		print('\n\tERROR: GRATING %i NOT RECOGNIZED' % grating)
		print('\tONLY 600 or 75 CURRENTLY ALLOWED')
		raise

	# For each frame, fit each of its peaks and get the 
	# peak's data (center, height, fwhm)
	tic = time.time()
	print('\tFINDING PEAK DATA...')
	for iPeak, peak in enumerate(peaks):
	    centers = np.zeros((len(frames), 2))
	    heights = np.zeros((len(frames), 2))
	    fwhms = np.zeros((len(frames), 2))

	    for iFrame, frame in enumerate(frames):
	        # Make copies so that pass by reference doesn't 
	        # cause modifications to data
	        y = np.copy(frame[peak[0]:peak[1]])
	        x_peak = np.copy(x[peak[0]:peak[1]])
	        [centers[iFrame,:],  # center wavelength and unc
	        heights[iFrame,:],   # center intensity and unc
	        fwhms[iFrame,:]] = LorentzFindPeak(x_peak, y)

	completed(tic)

	return heights, centers

###############################################################################


def plot_peak_2yaxis(centers, heights, output):


	'''
	Plot the intesity shift and wavelength shift of each frame
	relative to the first frame. Plotted on two y-axes with uncertainty band.
	'''

	# Plot the heights and centers (wavelength)
	fig, ax1 = plt.subplots()

	t = np.arange(0, 10*centers.shape[0], 10)
	y_height = heights[:, 0]/heights[0, 0]
	y_height_unc = heights[:, 1]/heights[0, 0]

	# Plot intensity shift of left y-axis
	ax1.plot(t, y_height, 'b-')
	ax1.fill_between(t, y_height-y_height_unc, y_height+y_height_unc,
					 color='b', alpha=0.5)
	ax1.set_xlabel('time (s)')
    # Make the y-axis label, ticks and tick labels match the line color.
	ax1.set_ylabel('Normalised Intensity', color='b')
	ax1.tick_params('y', colors='b', direction='in')

	ax1.tick_params('x', direction='in')

	# Plot wavelength shift on right y-axis
	y_center = centers[:, 0] 
	y_center_unc =  centers[:, 1] 

	ax2 = ax1.twinx()
	ax2.plot(t, y_center, 'r--')
	ax2.fill_between(t, y_center-y_center_unc, y_center+y_center_unc,
					 color='r', alpha=0.5)
	ax2.set_ylabel('Peak Wavelength Postion (nm)', color='r')
	ax2.tick_params('y', colors='r', direction='in')   
	ax2.set_ylim([995, 1003])

	fig.tight_layout()
	plt.savefig(output[:-4] + '.pdf')

	plt.close()


###############################################################################


def plot_peak_1yaxis(centers, heights, output):


	'''
	Plot the intesity shift and wavelength shift of each frame
	relative to the first frame. Plotted on two y-axes with uncertainty


	'''

	# Plot the heights (intensity relative to first frame)
	t = np.arange(0, 10*centers.shape[0], 10)
	y_height = heights[:, 0]/heights[0, 0]
	y_height_unc = heights[:, 1]/heights[0, 0]

	plt.plot(t, y_height, 'b-')
	plt.fill_between(t, y_height-y_height_unc, y_height+y_height_unc,
					 color='b', alpha=0.5)
	plt.xlabel('time (s)')
	plt.ylabel('Normalised Intensity')
	plt.tick_params('y', direction='in')
	plt.tick_params('x', direction='in')

	plt.tight_layout()
	plt.savefig(output[:-4] + '_INTENSITY.pdf')
	plt.close()

	# Plot centers (wavelength shift)
	y_center = centers[:, 0] 
	y_center_unc =  centers[:, 1] 

	plt.plot(t, y_center, 'r--')
	plt.fill_between(t, y_center-y_center_unc, y_center+y_center_unc,
					 color='r', alpha=0.5)
	plt.xlabel('time (s)')
	plt.ylabel('Peak Wavelength Postion (nm)')
	plt.tick_params('y', direction='in')   
	plt.ylim([995, 1003])
	plt.tick_params('x', direction='in')

	plt.tight_layout()
	plt.savefig(output[:-4] + '_WAVELENGTH.pdf')
	plt.close()


###############################################################################


def print_frame_data(centers, heights, samp_file):


	'''
	Print the intensity, its unc, the wavelength, and its unc of
	the photopeak at each frame
	'''

	# Write intensity and wavelength of peak maxes for each frame
	frame_data = open(samp_file[:-4] + '_FrameData.txt', 'w')

	frame_data.write('DATA FOR %s\n\n' % samp_file)

	frame_data.write('{0:6s}{1:>15s}{2:>15s}{3:>15s}{4:>15s}\n'.format(
		     'Frame', 'I_max', 'I_max_unc', 'lambda', 'lambda_unc'))
	# First frame
	frame_data.write('{0:6s}{1:>15.4e}{2:>15.4e}{3:>15.4e}{4:>15.4e}\n'.format(
					  "First", heights[0, 0], heights[0, -1],
					  centers[0, 0], centers[0, -1]))
	# Last Frame
	frame_data.write('{0:6s}{1:>15.4e}{2:>15.4e}{3:>15.4e}{4:>15.4e}\n\n'.format(
					  "Last", heights[-1, 0], heights[-1, -1],
					  centers[-1, 0], centers[-1, -1]))

	frame_data.write("DATA FOR ALL FRAMES:\n")

	frame_data.write('{0:6s}{1:>15s}{2:>15s}{3:>15s}{4:>15s}\n'.format(
		     'Frame', 'I_max', 'I_max_unc', 'lambda', 'lambda_unc'))
	for iFrame in range(centers.shape[0]):
		frame_data.write('{0:6n}{1:>15.4e}{2:>15.4e}{3:>15.4e}{4:>15.4e}\n'.format(
						  iFrame, heights[iFrame, 0], heights[iFrame, -1],
						  centers[iFrame, 0], centers[iFrame, -1]))
	frame_data.close()

