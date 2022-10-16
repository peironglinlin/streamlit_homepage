import streamlit as st
import pandas as pd
import numpy as np
import base64

from streamlit_option_menu import option_menu
import streamlit_nested_layout

from publications import publications
from scholar import n_citations

st.set_page_config(layout="wide")

def define_sidebar():
	with st.sidebar:
		select_sidebar = option_menu(None, ["Home", "Team",  "Research", 'Publications', 'Teaching','Presentations'], 
		    icons=['house', 'people', "gear", 'list-task', 'book','diagram-2-fill'], 
		    menu_icon="cast", default_index=0, orientation="vertical",
		    styles={
		        "container": {"padding": "0!important", "background-color": "#fafafa"},
		        "icon": {"color": "orange", "font-size": "25px"}, 
		        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
		        "nav-link-selected": {"background-color": "green"},
		    }
		)
	return select_sidebar

@st.experimental_memo(suppress_st_warning=True)
def load_home():
	tab1, tab2 = st.tabs(["Welcome", "News"])
	with tab1:
		st.header("Welcome to GeoWater's Homepage")
		col1, col2 = st.columns([6, 6])
		with col1:
			st.image("https://github.com/zkftyj/geowater_homepage/raw/main/animation.gif")

		with col2:
			st.markdown(f'<p style="background-color:#9FAAF8;color:#0C22BE;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">We study the geography of global inland waters, and we develop physically-based models, data-driven methods, and geographic information data infrastructures to improve our fundamental understanding of the river-climate and river-human relationships.</p>', unsafe_allow_html=True)
			st.error('I am always looking for highly motivated **PhD/master/undergraduate students** and **Postdoctoral Fellows** to work in my lab.')
			st.error('Please reach out to peironglinlin@pku.edu.cn if you are interested in working @ GeoWater lab @ PKU')
	with tab2:
		st.header("News")
		st.info('**2022-05: Undergraduate student Kaihao Zheng won the First Prize in the Challenging Cup competition for his research work on levee detection advised by Dr. Lin**. This competition consists of mostly masters or PhD students (can be in teams or single player), with less than 10% undergrads participating. Kaihao completed the competition on his own and won the award. **Big congratulations!** ')
		st.info('**2022-04-25: Co-authored paper published in Nature Sustainability!** Another work examining our rivers using an earth system science view, and a collaborative effort with the DryRiverRCN team, led by Corey Krabbenhoft. See article link here: https://www.nature.com/articles/s41893-022-00873-0. ')
		st.info('**2022-04: Water Resources Research Editors has recommended that I receive the 2021 Editors’ Citation for Excellence in Refereeing for Water Resources Research! Honored to receive such positive feedbacks as a reviewer.**')
		st.info('**2022-01: Peirong is joining Journal of Remote Sensing as a Young Editorial Board Member.**')


select_sidebar = define_sidebar()

if select_sidebar=="Home":
	load_home()

if select_sidebar=="Team":
	tab1, tab2, tab3 = st.tabs(["PI", "Graduate Students","Undergraduates"])
	with tab1:
		st.header("Prof. Peirong Lin")
		col1, col2 = st.columns([1.5, 6])
		with col1:
			st.markdown("#####")
			st.image("Team/PeirongLin.jpeg",width=150)
		with col2:
			tab_1,tab_2,tab_3 = st.tabs(["Current Position", "Professional Experiences","Academic Services"])
			with tab_1:
				col1, col2 = st.columns([6, 2])
				with col1:
					st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>Assistant Professor</b>, 2021-current
						<br>Institute of Remote Sensing and GIS, School of Earth and Space Sciences
						<br>Peking University
						<br><a href="https://scholar.google.com/citations?user=jCA3MkfZkRoC&hl=en">Google Scholar</a>
						</p>""", unsafe_allow_html=True)
				with col2:
					st.image('Team/Peking_University_logo.png',width=100)
				st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
					contact: <a href="peironglinlin@pku.edu.cn">peironglinlin@pku.edu.cn</a>
					</p>""", unsafe_allow_html=True)
			with tab_2:
				col1, col2 = st.columns([6, 2])
				with col1:
					st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>Postdoc</b>, 2018-2021
						<br>Department of Civil and Environmental Engineering,
						<br>Princeton University
						</p>""", unsafe_allow_html=True)
				with col2:
					st.image('Team/Princeton_University_log.png',width=200)
				col1, col2 = st.columns([6, 2])
				with col1:
					st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>Ph.D.</b>, 2012-2018
						<br>Water, Climate, and Environment (WCE) Program,
						<br>Jackson School of Geosciences,
						<br>The University of Texas at Austin
						</p>""", unsafe_allow_html=True)
				with col2:
					st.image('Team/ut_austin_logo.png',width=200)
				col1, col2 = st.columns([6, 2])
				with col1:
					st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>B.S. (honors)</b>, 2008-2012
						<br>Remote Sensing and Geographic Information Science,
						<br>Peking University
						</p>""", unsafe_allow_html=True)
				with col2:
					st.image('Team/Peking_University_logo.png',width=100)
			with tab_3:
				st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>NSF proposal reviewer</b>
						</p>""", unsafe_allow_html=True)
				st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>Journal Reviewer for</b> <a href="https://www.webofscience.com/wos/author/record/170368">(check publon)</a>
						<br> &bull; Geophysical Research Letters (4), 
						<br> &bull; Journal of Geophysical Research (2), 
						<br> &bull; Journal of Hydrology (2), 
						<br> &bull; Climatic Change (2), 
						<br> &bull; Journal of the American Water Resources Association (4), 
						<br> &bull; Weather and Forecasting (1), 
						<br> &bull; Advances in Meteorology (1), 
						<br> &bull; The Cryosphere (1), 
						<br> &bull; Environmental Modelling & Software (1), 
						<br> &bull; Hydrology and Earth System Sciences (1)
						</p>""", unsafe_allow_html=True)
	with tab2:
		pass

if select_sidebar=="Publications":
	style = """<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">"""
	tab1, tab2 = st.tabs(["Published", "Work in progress"])
	with tab1:
		tabs = st.tabs(['ALL'] + list(publications.keys()))
		with tabs[0]:
			col1, col2, col_, col_ = st.columns(4)
			with col1:
				n_total = np.array([len(publications[year]) for year in publications]).sum()
				st.metric(label="Total publications", value=n_total)
			with col2:
				st.metric(label="Total citations", value=n_citations)
			for i,year in enumerate(publications.keys()):
				st.subheader(year)
				for j,p in enumerate(publications[year]):
					rank = """<b>%s. </b>"""%(j+1)
					st.markdown(style+rank+p+"""</p>""", unsafe_allow_html=True)

		for i,year in enumerate(publications.keys()):
			with tabs[i+1]:
				for j,p in enumerate(publications[year]):
					rank = """<b>%s. </b>"""%(j+1)
					st.markdown(style+rank+p+"""</p>""", unsafe_allow_html=True)

if select_sidebar=="Teaching":
	col1,col2,col3 = st.columns(3)
	with col1:
		st.image('Teaching/course1.png')
		st.header('Earth System Modeling: Basics and Applications')
		st.subheader('(地球系统模式基础与应用)')
		st.info("Graduate Course (2 credits) Fall 2022")
	with col2:
		st.image('Teaching/course2.png')
		st.header('Spatio-Temporal Modeling and Analysis for Water Resources')
		st.subheader('(水资源时空模拟与分析)')
		st.info("Undergraduate Course (2 credits) Upcoming")
	with col3:
		st.image('Teaching/course3.png')
		st.header('GIS/RS/GPS Field Study')
		st.subheader('(3S野外实习)')
		st.info("Undergraduate Course (1 credit) Co-taught in Summer 2021")

if select_sidebar=="Research":
	st.warning("""
		I study the geography of global inland waters 

I use hydrologic models at unprecedented spatial resolution, space observations, and data-driven methods to understand the fundamentals of surface water dynamics and its feedback to the climate system. 

My research takes a holistic earth system view to understand the global inland waters and its related fields. 
""")

	tab1, tab2, tab3 = st.tabs(["1. Modeling and remote sensing of the global river continuum", 
						"2. Flood mechanisms and forecasting",
						"3. Land-atmosphere interaction"])
	with tab1:
		col1,col2 = st.columns(2)
		with col1:
			st.image('Research/Picture1.png')
			st.header('Reconstruction of naturalized river flows')
			st.info("Lin et al. (2019; WRR); this paper won the prestigious WRR Editor's Choice Award (given to 1% of papers annually)")
		with col2:
			st.image('Research/Picture2.png')
			st.header('Bankfull river width')
			st.info("Lin et al. (2020; GRL)")
	with tab2:
		col1,col2 = st.columns(2)
		with col1:
			st.image('Research/Picture3.png')
			st.header('Flood propagation speed influences flood peak')
			st.info("Lin et al. (2018; JHM)")
		with col2:
			st.image('https://github.com/zkftyj/geowater_homepage/raw/main/animation.gif')
			st.header('Large-scale fine-resolution flood simulation')
			st.info("Lin et al. (2018a, JHM; 2018b, EMS; 2018c, JAWRA)")
	with tab3:
		col1,col2,col3 = st.columns(3)
		with col1:
			st.image('Research/Picture4.jpeg')
			st.header('Snow hydrological/climatic effect')
		with col2:
			st.image('Research/Picture5.png')
			st.header('Snow-temperature')
			st.info("""Lin et al. (2016; GRL)
			Media report at: https://www.sciencedaily.com/releases/2016/12/161206111455.htm
			""")
		with col3:
			st.image('Research/Picture6.png')
			st.header('Snow-monsoon')
			st.info("""Lin et al. (2020; ERL)
			Media report at: https://www.sciencedaily.com/releases/2020/07/200716120705.htm
			""")


