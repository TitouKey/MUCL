"""Research catalogue used by seed.py.

Each entry is a dict with:
    title, authors, year, crew, category, disciplines, description, links

category values (drive the banner color):
    tech    -> red/orange
    health  -> green (health, biology)
    science -> blue (geology, physics, sciences)
    other   -> pink/mauve
"""

RESEARCH_DATA = [
    # ---------------------------------------------------------------
    # 2025 — Syrtis Crew
    # ---------------------------------------------------------------
    {
        "title": "Investigating arbuscular mycorrhizal fungi in a Martian-simulated environment",
        "authors": "Bérengère Bastogne",
        "year": "2025",
        "crew": "Syrtis Crew",
        "category": "health",
        "disciplines": ["Biology", "Microbiology", "Botany"],
        "description": (
            "The experiments conducted at the Mars Desert Research Station aimed to study the germination, "
            "viability and symbiotic efficiency of arbuscular mycorrhizal fungi (AMF) spores under simulated "
            "Mars conditions. The research investigated how AMF respond to environmental stresses: extreme "
            "temperatures, UV radiation, poor-nutrient soil (regolith) and gravity.\n\n"
            "The research was divided into two main experiments: an in vitro analysis of spore germination "
            "and viability and an in vivo evaluation of symbiotic efficiency.\n\n"
            "The first experiment consisted of testing the germination of AMF spores in Petri plates after "
            "exposure to simulated Martian stresses. A MTT test was also performed to assess spore viability "
            "following these stresses.\n\n"
            "The symbiotic efficiency of AMF spores with a host plant was evaluated in a second experiment. "
            "After exposure to the various conditions, spores were associated with roots of a host plant. "
            "Following a 10-day period, the host plant's root system was stained and analyzed microscopically "
            "to confirm the formation of a symbiotic association.\n\n"
            "Additionally, soil samples were collected from the Mars Desert Research Station to examine the "
            "presence of AMF and their stress tolerance."
        ),
    },
    {
        "title": "Crisis Resource Management on Mars",
        "authors": "Odile Hilgers",
        "year": "2025",
        "crew": "Syrtis Crew",
        "category": "health",
        "disciplines": ["Medicine", "Emergency care", "Simulation"],
        "description": (
            "As the Health and Safety Officer of the Syrtis Crew, I explored the application of Crisis "
            "Resource Management (CRM) principles during simulated medical emergencies in a Mars analog "
            "environment. This study involved six simulations of cardiac arrest, designed to reflect the "
            "operational and psychological constraints of long-duration space missions. The eight-member "
            "crew, all trained in Basic Life Support (BLS) prior to deployment, responded to varied cardiac "
            "arrest scenarios reflecting different underlying causes.\n\n"
            "The protocol included two initial training simulations, followed by two \"Earth\" scenarios—with "
            "assumed remote support—and two \"Mars\" scenarios simulating full autonomy, conducted without "
            "prior warning to preserve realism and cognitive stress. Team performance was assessed using the "
            "Ottawa Global Rating Scale (Ottawa GRS), a validated CRM evaluation tool measuring leadership, "
            "communication, situational awareness, problem-solving, and resource management. Objective data, "
            "including time to recognition, initiation of chest compressions, and delivery of the first shock "
            "with a training automated external defibrillator (AED), were systematically collected.\n\n"
            "Following each simulation, structured debriefings provided qualitative insight into perceived "
            "team efficiency, stress management, and confidence. By combining behavioral assessment with "
            "objective performance metrics, this study offers a structured framework to analyze non-technical "
            "skills in extreme environments.\n\n"
            "These findings aim to support the integration of CRM-based simulation training in both space "
            "medicine preparation and terrestrial critical care contexts, where high-performance teamwork "
            "under pressure is essential for patient outcomes."
        ),
    },
    {
        "title": "HIIT vs Endurance Training: Which Exercise Modality Best Supports Astronaut Concentration During Long-Duration Missions?",
        "authors": "Béatrice Hollander · Arnaud de Wergifosse",
        "year": "2025",
        "crew": "Syrtis Crew",
        "category": "health",
        "disciplines": ["Physiology", "Exercise science", "Cognitive science"],
        "description": (
            "We aimed at identifying which type of physical exercise may provide greater benefits to "
            "astronauts during long-duration missions, such as future expeditions to Mars. In this study, we "
            "sought to compare the effects of two exercise modalities performed on a cycle ergometer—high-"
            "intensity interval training (HIIT) and low-intensity steady-state endurance training (EF)—on "
            "attentional processes. Maintaining optimal concentration and cognitive performance in such "
            "environments is critical for mission success and crew safety.\n\n"
            "Each experimental day began with the collection of baseline data. Participants' sleep parameters "
            "and blood glucose levels were recorded in the morning to provide contextual and physiological "
            "indicators prior to exercise. Following this, they completed the training protocol assigned for "
            "that cycle (three consecutive days of either HIIT or EF). During each exercise session, heart "
            "rate (HR) was continuously monitored, and participants were asked to report their perceived "
            "exertion.\n\n"
            "At the end of each three-day cycle, we assessed attentional performance using the Stroop test, "
            "which measures the ability to concentrate and process visual information under conditions of "
            "cognitive interference. At the same time, a galvanometer was used to record electrodermal "
            "responses, providing an objective measure of autonomic nervous system activity and, more "
            "specifically, stress levels during the task.\n\n"
            "In addition, standardized questionnaires on sleep quality and baseline stress were administered "
            "to control for potential confounding variables.\n\n"
            "Taken together, this protocol was designed to provide a comprehensive evaluation of how "
            "different exercise modalities influence attentional processes."
        ),
    },
    {
        "title": "Bacterial Survival Under Martian Conditions",
        "authors": "Batoul Tani",
        "year": "2025",
        "crew": "Syrtis Crew",
        "category": "health",
        "disciplines": ["Microbiology", "Astrobiology"],
        "description": (
            "During the Syrtis M.A.R.S UCLouvain Mission, I investigated the survival mechanisms of two model "
            "bacteria, Escherichia coli and Bacillus thuringiensis, when exposed to stresses related to "
            "Martian environmental conditions.\n\n"
            "In space, astronauts are isolated, and a bacterial contamination can potentially be fatal. Two "
            "bacterial phenomena are particularly concerning in this context: biofilm formation (antibiotic "
            "resistance, water contamination, and clogging of pipes) and sporulation (highly resistant "
            "structures that promote transport and wide dispersion of bacteria).\n\n"
            "First, for Escherichia coli, I studied the growth and resistance of its biofilm under different "
            "conditions: presence or absence of bacteriophages (viruses that infect bacteria and represent a "
            "promising alternative to antibiotics), exposure to UV-C radiation, and stable versus fluctuating "
            "temperatures.\n\n"
            "Then, for Bacillus thuringiensis, I examined its ability to form spores. These structures enable "
            "the bacterium to survive and protect itself from many adverse environmental factors (such as "
            "drought and extreme temperatures). In this case, the bacterium was also exposed to UV radiation "
            "and temperature variations, and I sought to determine whether the presence of soil in the medium "
            "would protect it or instead promote sporulation."
        ),
    },
    {
        "title": "Impact of Martian dust on infrastructure durability",
        "authors": "Antoine Dubois",
        "year": "2025",
        "crew": "Syrtis Crew",
        "category": "tech",
        "disciplines": ["Engineering", "Materials science"],
        "description": (
            "Following the experiment conducted by Maxime Foucart last year, my study will focus on assessing "
            "the hazards posed by Martian dust to infrastructure, particularly a Martian base. The aim is to "
            "characterize the particle size distribution of dust transported close to the ground, by measuring "
            "its distribution every 10 cm up to a height of 30 cm. Coarse particles, which are more abrasive "
            "than finer ones, represent a significant threat to the integrity of materials during long-term "
            "missions. This experiment aims to determine the height at which structures should be reinforced "
            "in order to mitigate the abrasive effects of aeolian dust transport."
        ),
    },
    # ---------------------------------------------------------------
    # 2024 — Atlas Crew
    # ---------------------------------------------------------------
    {
        "title": "Dust Understanding for Solar Technology Yield (DUSTY)",
        "authors": "Maxime Foucart",
        "year": "2024",
        "crew": "Atlas Crew",
        "category": "tech",
        "disciplines": ["Engineering", "Solar energy", "Meteorology"],
        "description": (
            "Space is a dangerous and relentless environment, throwing challenges to everybody who dares "
            "venture into the unknown. Collecting and understanding data from an alien world is key to "
            "survival, that is why my experiment is going to be about the study of the danger of dust from "
            "Martian storms. These storms are not very well understood and the dust they pick up can be "
            "hazardous for vital equipment such as the solar panels. I will use two weather stations that "
            "will track luminosity, air pressure, wind speed and temperature for two weeks and use my mapping "
            "skills to figure out if the environment around the MDRS is suitable for sensitive equipment or "
            "not. One of the weather stations will be stationary during the two weeks and the other will be "
            "mobile, moved each day to a new location to try and gauge the exposition to dust and wind."
        ),
    },
    {
        "title": "Mapping the Martian Frontier: High-Fidelity Topographic Perspectives for Strategic Landing Site Selection",
        "authors": "Louis Joseph",
        "year": "2024",
        "crew": "Atlas Crew",
        "category": "science",
        "disciplines": ["Geomatics", "Photogrammetry", "Topography"],
        "description": (
            "An overlooked aspect of a Mars exploration mission is the selection of the landing site "
            "location. Whether it is for the initial landing, or for the establishment of a base, the chosen "
            "location must meet a lot of mission-critical criteria. Most orbital-produced topographic maps of "
            "Mars suffer from a lack of spatial resolution. My research project will hence be focused on the "
            "production of high-fidelity topographic maps of the study area using a method known as "
            "photogrammetry, along with UAV (unmanned aerial vehicle) technology."
        ),
    },
    {
        "title": "Isolation Insights: A Psychological Expedition into Mars Crew Dynamics",
        "authors": "Loriane Baes",
        "year": "2024",
        "crew": "Atlas Crew",
        "category": "other",
        "disciplines": ["Psychology"],
        "description": (
            "Human behavior has always intrigued me. So I decided to bring a touch of psychology to the "
            "experiment. My experiment will therefore involve obtaining very detailed profiles of the crew "
            "members through personality tests, in order to analyze how these different personality types "
            "deal with the group's isolation during the potentially stressful MARS experience."
        ),
    },
    {
        "title": "Lactobacillus Helveticus on sleep and stress in space missions",
        "authors": "Arnaud de Wergifosse · Imane El Bakkali",
        "year": "2024",
        "crew": "Atlas Crew",
        "category": "health",
        "disciplines": ["Microbiology", "Health", "Neuroscience"],
        "description": (
            "The isolation experienced by astronauts during their space missions can cause stress. The aim of "
            "the study is to evaluate the impact of Lactobacillus Helveticus administration on containment "
            "stress. The study will be composed of 2 groups. One group will receive Lactobacillus Helveticus "
            "and another group will receive a placebo for two weeks before, during, and after the "
            "simulation.\n\n"
            "Different markers, including cardiac, hormonal, and inflammatory markers, will be measured at "
            "different times. The medical application designed for astronauts, EveryWear, will also be "
            "utilized to record various parameters, such as heart rate and sleep."
        ),
    },
    {
        "title": "Building the Future on Mars: In-Situ Reaction Synthesis for Sustainable Colonies",
        "authors": "Romain Maddox",
        "year": "2024",
        "crew": "Atlas Crew",
        "category": "science",
        "disciplines": ["Chemistry", "Materials science"],
        "description": (
            "Thanks to the previous work done by fellow scientists, I will first write a paper on the "
            "synthesization of sustainable colonies based on in-situ reaction at different key localization. "
            "Based on my theoretical approach, I will then create, demonstrate and test different physical "
            "and chemical processes to confirm the validity of my theoretical work."
        ),
    },
    {
        "title": "AI-Powered Mission Support",
        "authors": "Hippolyte Hilgers",
        "year": "2024",
        "crew": "Atlas Crew",
        "category": "tech",
        "disciplines": ["Artificial intelligence", "Software engineering"],
        "description": (
            "During the M.A.R.S. UCLouvain mission, team members will be confronted with an unpredictable "
            "environment. A great deal of preparation is required to cope with unexpected situations. To "
            "support the crew and help them carry out tasks and make the right decisions, I propose to use an "
            "artificial intelligence (AI) stored locally on a computer.\n\n"
            "The AI would be trained throughout the year with mission information, such as scientific "
            "objectives, technical constraints and safety protocols. In this way, it could provide useful "
            "information and advice tailored to the specific circumstances of the mission.\n\n"
            "AI could be used as a tool similar to ChatGPT, enabling team members to ask questions and get "
            "answers quickly and easily. It could also be used to monitor environmental conditions and report "
            "any significant changes that might affect the mission.\n\n"
            "To take the idea a step further, I propose transforming the AI into a voice assistant using a "
            "program. This would enable team members to communicate with it without having to use a keyboard "
            "or screen, which could be particularly useful during spacewalks or in other situations where "
            "the hands are busy."
        ),
    },
    {
        "title": "Lactobacillus Helveticus on the immune system in space missions",
        "authors": "Alba Sanchez Montalvo",
        "year": "2024",
        "crew": "Atlas Crew",
        "category": "health",
        "disciplines": ["Immunology", "Microbiology"],
        "description": (
            "Scientists know that certain factors related to spaceflights may impact the immune system of "
            "astronauts, such as microgravity but also radiation exposure, isolation, and stress. Also, a "
            "dysregulation occurs in astronauts' immunity (pro-inflammatory and Th1 responses) during "
            "long-term spaceflight. The goal of my study is to evaluate the immune system function before, "
            "during and after the mission at the MDRS. Blood and saliva samples will be collected from the "
            "participants and antibody (IgM, IgD, IgG, IgA, IgE) and cytokine (Th1/Th2/Th17 profiles) "
            "production will be measured. Before and after the mission, stimulation assays to study the "
            "ability of immune cells, such as neutrophils, B and T cells, to respond to different stimulus "
            "will be performed. These biomarkers may be useful to monitor the effectiveness of biomedical "
            "countermeasures for astronauts, with potential application in terrestrial research."
        ),
    },
    # ---------------------------------------------------------------
    # 2023 — Ares Crew
    # ---------------------------------------------------------------
    {
        "title": "Study on Mars radiation",
        "authors": "Thomas Stinglhamber",
        "year": "2023",
        "crew": "Ares Crew",
        "category": "science",
        "disciplines": ["Physics", "Radiation", "Dosimetry"],
        "description": (
            "The radiation is invisible and odorless. The martionauts on Mars will have to face this "
            "invisible enemy much more than we on Earth. So how do you protect them? By deploying a whole "
            "series of dosimeters. Each person will have 1, 1 will be put outside, 1 inside, 1 underground "
            "and 1 in Belgium to compare the different doses to a reference. All this will allow me to "
            "calculate the effectiveness of the shielding of the station as well as of the ground and above "
            "all to establish a threshold for the martionauts. In addition, thanks to a NaI scintillator, I "
            "will map the surroundings of the base to make a 3D map. I will collect samples from the places "
            "with the most radiation to do analyses in Belgium to find out what the isotopes are and in what "
            "proportion."
        ),
    },
    # ---------------------------------------------------------------
    # 2023 — Atlas Crew
    # ---------------------------------------------------------------
    {
        "title": "Study of the biocompatibility of the Martian environment for Terrestrial organisms",
        "authors": "Agnès Dekeyser",
        "year": "2023",
        "crew": "Atlas Crew",
        "category": "health",
        "disciplines": ["Astrobiology", "Extremophiles"],
        "description": (
            "Terraforming Mars? Why? Well, because life as we know it cannot survive Mars' extreme "
            "conditions. But that may not be entirely true. Indeed, some organisms on Earth have the ability "
            "to survive conditions that are lethal to most other organisms, they are called extremophiles. "
            "But could they withstand Mars' extreme conditions? This is the question this study aims to "
            "answer.\n\n"
            "Extremophiles will be exposed to the environmental conditions found at the MDRS site simulating "
            "the pressure, temperature and radiation found on Mars. At different time points, their viability "
            "will be assessed and compared to that of their unexposed analogues.\n\n"
            "Understanding how these organisms manage to survive such extreme conditions could lead to "
            "interesting research, such as studying how we could use their ability to facilitate habitation "
            "on Mars for humans as well as for plants or animals."
        ),
    },
    {
        "title": "Study on the influence of the specific nutrition of astronauts on the microbiota",
        "authors": "Antoine de Barquin",
        "year": "2023",
        "crew": "Atlas Crew",
        "category": "health",
        "disciplines": ["Nutrition", "Microbiology"],
        "description": (
            "Thanks to an experiment previously carried out on astronauts, we know that containment has an "
            "impact on our microbial flora that we call our \"second brain\". But containment will not be the "
            "only parameter to have an impact on our micro-organisms. The specific food of the astronauts is "
            "obviously a major element and my experiment will consist in studying the changes on our "
            "microbiota caused by this specific food."
        ),
    },
    {
        "title": "Exploring Drone Utility for Radiation Protection on Martian Ground and Underground",
        "authors": "Augustin Tribolet",
        "year": "2023",
        "crew": "Atlas Crew",
        "category": "science",
        "disciplines": ["Radiation", "Physics", "Robotics"],
        "description": (
            "One of the greatest challenges for manned missions to Mars is the high radiation environment "
            "that exists in space. Unlike Earth, Mars has a very weak magnetic field and an extremely thin "
            "atmosphere, which does not offer sufficient protection against incoming radiation. A promising "
            "strategy is to use the Martian ground and underground as a natural shield against such level of "
            "radiation. To this end, this project explores the feasibility of using a drone as a valuable "
            "tool for locating and analysing potential entrances to the underground. During the maximum "
            "activity of the sun, there are extreme solar events that can also contribute to radiation on "
            "Mars. In particular, coronal mass ejections unpredictably eject large amounts of energetic "
            "particles into space. Under certain conditions, the particles can reach the surface of Mars and "
            "could surprise astronauts during an extravehicular activity. The idea here is to use the drone "
            "to see how to make the best use of the terrain to be protected from these unpredictable events."
        ),
    },
    {
        "title": "Development of the emergency procedure",
        "authors": "Gwenaël le Bussy",
        "year": "2023",
        "crew": "Atlas Crew",
        "category": "other",
        "disciplines": ["Safety", "Emergency management"],
        "description": (
            "The Martian environment is not suitable for the survival of human beings. So, what would happen "
            "if the protective layer around the astronauts were to be damaged? Then our astronauts would be "
            "exposed to the greatest of dangers. They must react fast to guarantee the mission survival. "
            "Therefore, a simple and explicit procedure must be defined if something were to happen inside "
            "the station. It will be based on multiple factors: participants personality, compilation on the "
            "safety standards, inventory on goods and equipment on site, implementation of fake scenarios, "
            "first aid procedures and so on. All the astronauts will participate actively in the development "
            "of this procedure to make it easy and durable."
        ),
    },
    {
        "title": "Study of psychological and behavioral adaptation to isolated and confined environments",
        "authors": "Ttele Hiriart",
        "year": "2023",
        "crew": "Atlas Crew",
        "category": "other",
        "disciplines": ["Psychology"],
        "description": (
            "I have always been interested in people's relationships and interactions. Creating a strong and "
            "united crew is not easy when you start with a team of foreigners. By completing questions "
            "files, making several exercises, mental games and using actual psychological tools I would like "
            "to analyze the personalities, emotions, desires, expectations, and fears of my teammates. Also, "
            "studying people's behavior can lead to some answers in the interpretation of their reactions in "
            "front of different situations. This would make easier the creation of our own tools to get well "
            "together and be able to resolve internal problems. I think it is essential to respect the "
            "wellbeing of everyone and to understand the different needs of one another. All that in the aim "
            "of creating a working together team who can count on each other."
        ),
    },
    {
        "title": "Space Oddity: reducing stress with music?",
        "authors": "Ioana Dimitrova",
        "year": "2023",
        "crew": "Atlas Crew",
        "category": "other",
        "disciplines": ["Psychology", "Stress management"],
        "description": (
            "Confinement and isolation is difficult for every crew that leaves the Earth. It leads to stress "
            "that can impact the body in a negative way, psychologically but also physically by increasing "
            "cortisol and blood pressure levels. One solution to this problem could be listening to music; "
            "it's pleasant and not a complicated strategy to implement! I will thus be studying how listening "
            "to recorded and live music can help reduce this stress and how it can positively impact the "
            "astronauts stay in space!"
        ),
    },
    {
        "title": "Study on the isolation of social networks",
        "authors": "Aglaé Sacré",
        "year": "2023",
        "crew": "Atlas Crew",
        "category": "other",
        "disciplines": ["Psychology", "Social sciences"],
        "description": (
            "We are constantly connected to social networks and information. So connected that sometimes our "
            "relationships with others are impacted. So what would be the impact on us and our relationships "
            "with others by being disconnected for 2 weeks as part of a life simulation on Mars. For this, I "
            "will study the individual use of each person before, study the relationships between us during "
            "and then analyze the after and our relationship to social networks and information. The second "
            "part of my experiment will be to test our reflexes. We will be submitted to a stressful "
            "environment, to fatigue, ... will these factors influence our reaction time. This study will be "
            "conducted on the basis of a software with exercises to test our reflexes."
        ),
    },
    # ---------------------------------------------------------------
    # 2022 — Tharsis Crew
    # ---------------------------------------------------------------
    {
        "title": "Terrain modelling by Synthetic Aperture Radar",
        "authors": "Cyril Wain",
        "year": "2022",
        "crew": "Tharsis Crew",
        "category": "tech",
        "disciplines": ["Engineering", "Remote sensing", "Radar"],
        "description": (
            "As part of a study on Synthetic Aperture Radar (SAR), an imaging campaign will be conducted. "
            "SAR is a form of radar used to create 2D images or perform 3D reconstructions of objects or "
            "landscapes. Its principle relies on motion to obtain radar images with very high resolution. "
            "This type of radar is typically deployed on airplanes or satellites.\n\n"
            "The main advantage of SAR is that, unlike optical sensors, it is not affected by weather "
            "conditions. Since it operates in the microwave frequency band, its waves easily penetrate clouds "
            "and rain. This makes SAR a valuable tool for studying the topography of planets where weather "
            "conditions—such as clouds, heavy rain, or sandstorms—would hinder observation through optical "
            "sensors.\n\n"
            "The imaging campaign will allow the study to test an image reconstruction algorithm in real "
            "conditions."
        ),
    },
    {
        "title": "Assessment of metabolic changes due to alterations in physical activity and nutrition",
        "authors": "Jean Jacobs",
        "year": "2022",
        "crew": "Tharsis Crew",
        "category": "health",
        "disciplines": ["Physiology", "Nutrition"],
        "description": (
            "Mars colonization is not only a technological challenge but also a physical challenge for future "
            "marstronauts. Microgravity, environmental conditions, and changes in nutrition will have a "
            "significant impact on the crew's health.\n\n"
            "The study aims to develop a protocol for monitoring essential health and metabolic parameters of "
            "crew members. The data collected will help provide recommendations on food intake, physical "
            "activity, and the early detection of disease signs."
        ),
    },
    {
        "title": "Study of the effect of biofertilizers on the germination rate of edible plants of interest in a Martian soil substrate",
        "authors": "Cheyenne Chamart",
        "year": "2022",
        "crew": "Tharsis Crew",
        "category": "health",
        "disciplines": ["Botany", "Agronomy", "Biology"],
        "description": (
            "The study focuses on plant biology and physiology, particularly in the context of food supply "
            "for a crew living in complete autarky on Mars. With expertise in plant experiments and "
            "greenhouse environments, the research aims to explore solutions for sustaining plant growth in "
            "extraterrestrial conditions.\n\n"
            "To analyze the growth of edible plants, various parameters can be considered, including biotic "
            "factors (use of biofertilizers, impact of the absence of soil fauna on plant development and "
            "organic matter decomposition) and abiotic factors (low temperatures and pressure, reduced oxygen "
            "levels, perchlorate-rich soil similar to that of Mars, and growth in \"rocky soil\" sampled from "
            "the field). Given the total absence of fauna in Martian soil, the study will specifically focus "
            "on the use of biofertilizers (composed of microorganisms) and their effect on the germination "
            "rate of edible plant species of interest, such as Solanum tuberosum (potato) for its high "
            "starch and fiber content, as well as alfalfa and tomato. Since the number of seeds available at "
            "the start of space missions must be optimized, minimizing losses is crucial.\n\n"
            "The experiment aims to determine how, in a Mars station—such as the closed environment of the "
            "MDRS station—and with a Martian regolith-like substrate, biofertilizers in small quantities "
            "could help meet the caloric needs of a crew. If time and space allow, additional experiments on "
            "other biotic and abiotic factors mentioned above may also be conducted."
        ),
    },
    {
        "title": "Sleeping Hypnosis experiment",
        "authors": "Julien Meert",
        "year": "2022",
        "crew": "Tharsis Crew",
        "category": "health",
        "disciplines": ["Medicine", "Sleep research"],
        "description": (
            "Based on previous experiments at the MDRS, it has been observed that the sleep quality of an "
            "astronomer in the station is not as good as at home. This study aims to explore whether "
            "hypnosis techniques, similar to those used in medicine before sleep, could help improve sleep "
            "depth and quality.\n\n"
            "By enhancing sleep, these techniques could contribute to ensuring that astronomers have the "
            "necessary energy for their demanding tasks in the following days."
        ),
    },
    {
        "title": "In-situ fracture fixation for space missions",
        "authors": "Julie Manon",
        "year": "2022",
        "crew": "Tharsis Crew",
        "category": "health",
        "disciplines": ["Medicine", "Biomedical engineering"],
        "description": (
            "Imagine a mission on Mars where an astronaut suffers an accident or trauma during an EVA, "
            "requiring surgery and making repatriation to Earth impossible. Wouldn't it be revolutionary to "
            "have a device capable of treating the injury on-site, without the need for a surgeon?\n\n"
            "This study aims to explore such a solution at the MDRS during this mission. The goal is to "
            "develop a low-cost fixator that is accessible, quick to implement, and easily usable by any "
            "astronaut without surgical training. By doing so, space exploration could mitigate the risks of "
            "fractures that might otherwise prove fatal in such an extreme environment."
        ),
    },
    {
        "title": "Evaluate different living conditions in the breeding of insects in order to integrate them into the astronauts' diet",
        "authors": "Sirga Drouet",
        "year": "2022",
        "crew": "Tharsis Crew",
        "category": "health",
        "disciplines": ["Biology", "Nutrition", "Entomology"],
        "description": (
            "This study aims to contribute to improving the nutritional quality of a future crew of "
            "astronauts by exploring an alternative food solution with high yield, minimal space "
            "requirements, and low energy consumption: insect farming.\n\n"
            "Insects present several advantages over other living organisms, including lower water "
            "consumption, reduced space requirements, and minimal greenhouse gas emissions. However, their "
            "greatest asset is their high food conversion efficiency.\n\n"
            "The experiment will focus on evaluating the viability and yield rate of three insect species—"
            "belonging to the orthoptera, beetle, and lepidopteran groups—under the living conditions of the "
            "Martian simulation station. These results will be compared with a terrestrial control model to "
            "assess the feasibility of insect farming as a sustainable food source for long-duration space "
            "missions."
        ),
    },
    {
        "title": "Bio-printing for space medicine",
        "authors": "Ignacio Sánchez Casla",
        "year": "2022",
        "crew": "Tharsis Crew",
        "category": "health",
        "disciplines": ["Biomedical engineering", "3D printing"],
        "description": (
            "3D printing is a relatively new technology with endless possibilities. Easily scalable and "
            "transportable, it is likely that future marstronauts will bring multiple 3D printers to our "
            "sister planet.\n\n"
            "This study will focus on 3D printing scaffolds using bio-ink to seed stem cells, followed by "
            "mechanical stress-strain tests on the resulting micro-architecture. The goal is to explore the "
            "potential of 3D-printed biological structures in the context of space missions, where in-situ "
            "fabrication could be crucial for medical and research applications."
        ),
    },
    # ---------------------------------------------------------------
    # Crew 227 — 2020/21
    # ---------------------------------------------------------------
    {
        "title": "Study of the survival of human flora bacteria as well as efficacy of several antibiotics under Martian environmental conditions",
        "authors": "Audrey Comein · Kilian Dekoninck",
        "year": "2020/21",
        "crew": "Crew 227",
        "category": "health",
        "disciplines": ["Microbiology", "Pharmacology"],
        "description": (
            "When humans colonize Mars, they will not come alone: the microorganisms of the intestinal, oral, "
            "and cutaneous flora will accompany them. It is therefore essential to predict what types of "
            "microorganisms in these floras would be able to survive and colonize Mars.\n\n"
            "The study will focus on analyzing the survival and growth capacity of bacteria collected from "
            "the crew and exposed to the environmental conditions found on the MDRS site. These harvested "
            "bacteria will be identified by proteomic analysis. The exposed bacteria will be compared "
            "directly to their unexposed analogues based on CFUs (Colony-Forming-Units) analysis. This "
            "analysis will determine the number of bacteria per milliliter of sample for each bacterium "
            "collected. Comparing this value between exposed and non-exposed bacteria will reveal which "
            "types of bacteria in the human flora could potentially colonize Mars.\n\n"
            "If some of these bacteria can survive on Mars, they could potentially cause infections in the "
            "human colony. Therefore, the question to be addressed is: which antibiotics would remain "
            "sufficiently functional under such conditions?\n\n"
            "To answer this question, the study will evaluate the efficacy of antibiotics from different "
            "classes exposed to environmental conditions and compare them to the same unexposed antibiotics. "
            "Antibiotic efficacy will be estimated based on the minimum concentration required to inhibit "
            "bacterial growth: the lower this concentration, the more effective the antibiotic. Thanks to "
            "this experiment, it will be possible to determine which antibiotics to bring to Mars."
        ),
    },
    {
        "title": "Data collection and transmission over low-powered devices for station monitoring",
        "authors": "Brieuc de Voghel",
        "year": "2020/21",
        "crew": "Crew 227",
        "category": "tech",
        "disciplines": ["Engineering", "Electronics", "Networking"],
        "description": (
            "By installing a series of low-powered sensors and transmitters, it will be possible to model "
            "the MDRS's environment and extra-vehicular activities (temperature, humidity, pressure, "
            "brightness, etc.) in order to detect variations in the habitat, the greenhouse and along "
            "expeditions. The objective is to collect, transmit and analyze the data as efficiently as "
            "possible as we try to adapt to the harsh Martian conditions. The data can be used to prepare "
            "and monitor other experiences.\n\n"
            "A Martian mission involves a lot of risks and hardware must therefore be extremely reliable. To "
            "check the reliability of certain objects used during the mission, we will use a series of "
            "Zigbee transmitters capable of transmitting information about the status of the monitored "
            "devices. Zigbee transmitters are low-power, low-cost radios that can transmit data over long "
            "distances through a network of intermediate transmitters in order to reach more distant ones. "
            "Such radios are currently used for home automation, data collection in medical devices, etc.\n\n"
            "The low-power transmitters could be extremely useful in a hostile environment like Mars where "
            "batteries cannot be changed frequently or where low power consumption is of high importance.\n\n"
            "In addition, the data collected by sensors, and transmitted through the Zigbee devices, will "
            "provide insight about the status of the EVA suits, the rovers, the GreenHab, etc. The data "
            "would then be analysed to understand the condition of the monitored equipment. Data anomalies "
            "would thus result in warnings which would inform the crew that repairs are required."
        ),
    },
    {
        "title": "Study of the efficacy of a potential living-antibiotic, the bacterium Bdellovibrio bacteriovorus, inside and outside a research station in a Mars-like environment",
        "authors": "Ophélie Rémy",
        "year": "2020/21",
        "crew": "Crew 227",
        "category": "health",
        "disciplines": ["Microbiology"],
        "links": [
            {
                "label": "Raghunathan et al. (2019) — Engulfment, persistence and fate of Bdellovibrio bacteriovorus (Scientific Reports)",
                "href": "https://doi.org/10.1038/s41598-019-40223-3",
            }
        ],
        "description": (
            "Due to its particularity of killing other bacteria without killing human cells, Bdellovibrio "
            "bacteriovorus is being studied as a serious alternative to antibiotics, especially against "
            "resistant strains. Moreover, unlike antibiotics, its effectiveness over time does not diminish, "
            "which is particularly relevant for long-term travel such as the transport and establishment of "
            "a colony on Mars.\n\n"
            "The project I, Ophélie Rémy, would like to lead to the Mars Desert Research Station is about "
            "Bdellovibrio bacteriovorus. This small bacterium (max 1 µm) has the particularity of feeding on "
            "a wide range of other bacteria. This predator is currently being studied by several scientific "
            "teams as a real alternative to antibiotics because the bacteria-prey can't develop resistance "
            "against it and it does not attack the cells of the human body [1].\n\n"
            "Given the consequent duration of travel and potential stays on Mars, storage and management of "
            "perishable products such as antibiotics are significant logistic and biomedical parameters. "
            "However, using Bdellovibrio as a future alternative, these problems would be greatly reduced. "
            "Indeed, instead of storing various types of antibiotic boxes, which are useless after 2 or 3 "
            "years, only a few tubes of frozen bacteria and medium can generate an infinite number of "
            "daughter bacteria.\n\n"
            "There is nevertheless a constraint for its proliferation: prey. That's why, within the two-week "
            "time limit, my goals will be to isolate bacteria from the cockpit space, from the environment "
            "(if possible) or directly from the crew (saliva, skin, etc.), grow them, identify them, give "
            "them as prey to Bdellovibrio bacteria and observe which strains are thus exploitable as easily "
            "accessible resources for this predatory bacterium.\n\n"
            "Compare the efficiency of the predator Bdellovibrio to kill their preys under various extreme "
            "conditions to test if the culture of these bacteria is easily achievable in an environment more "
            "hostile than the ideal conditions of a laboratory.\n\n"
            "[1] Raghunathan D. et al. (2019) Engulfment, persistence and fate of Bdellovibrio bacteriovorus "
            "predators inside human phagocytic cells informs their future therapeutic potential. Scientific "
            "reports. 9:4293, 1-16. DOI: 10.1038/s41598-019-40223-3."
        ),
    },
    {
        "title": "Fast assessment of mineral content on Martian-like soil with portable XRF device",
        "authors": "Arthur Monhonval · Elizabeth Mauclet",
        "year": "2020/21",
        "crew": "Crew 227",
        "category": "science",
        "disciplines": ["Geology", "Geochemistry", "Soil science"],
        "description": (
            "This experiment is about testing an innovative way to analyze Martian soil composition. At the "
            "MDRS, our goal is to provide a rapid and reliable assessment of Martian-like mineral content, "
            "which will contribute (i) to evaluating the suitability of these soils for food production and "
            "(ii) to study the potential ancient presence of liquid water pathways. To meet this objective, "
            "we will use a portable X-ray fluorescence (pXRF) device, already used for terrestrial soil "
            "mineral content analysis. Thanks to its portability, its large range of mineral detection or "
            "even its rapidity, the pXRF seems to show powerful advantages to tackling questions still "
            "unanswered about Martian soil surface composition. Our experiment will implement guidelines to "
            "reproduce these measurements on Mars in coming decades and its actual mineral content, at a "
            "small-scale.\n\n"
            "The experience we will lead at the MDRS is the study of mineral content of Martian-like soils. "
            "We would like to test a rapid and reliable method, already used for terrestrial soils, to "
            "assess the mineral content of Martian-like soil surface.\n\n"
            "This will fulfill two sub-questions we address:\n\n"
            "(1) How suitable are Martian soils for food production?\n"
            "Because of their essential role in human survival, soil quality on Earth is highly studied all "
            "around the world. Indeed, soil contamination with metals or toxic components may have dangerous "
            "consequences on human health. In a context of Mars colonization, if someday people are expected "
            "to live on Mars, could they rely on a \"local\" food production? Do those soils contain the "
            "minimal required concentration of essential plant nutrients? Do they contain too high "
            "concentration of toxic elements (such as Pb, As, Cd) making food production unsuitable for the "
            "human diet?\n\n"
            "(2) Can we identify ancient preferential liquid water pathways?\n"
            "By studying the element distribution at a soil-profile scale, we will be able to highlight the "
            "mineral element mobility through a soil profile. On Earth, mineral mobility is driven by water "
            "and wind transport, vegetation cycling, etc. As Martian environment does not present any "
            "current vegetation or life, liquid water transport seems to be the only potential driver of "
            "minerals mobility through vertical and lateral fluxes. According to their solubility, specific "
            "elements are more relevant to study because they are more susceptible to dissolving and are "
            "taken away by the liquid water. By studying the element concentration distribution along soil "
            "profiles at different locations, their variability will allow us to observe their mobility and "
            "assess the potential presence of liquid water fluxes. The aim is to imagine a transposable "
            "protocol on future Martian rovers, to reproduce it up there and study the potential ancient "
            "presence of liquid water... and therefore potential ancient Life!\n\n"
            "How does a pXRF device work and what are its advantages?\n"
            "The portable X-Ray Fluorescence device relies on the X-ray fluorescence principle to quantify "
            "the concentration of mineral element in a sample. It allows us to detect every element from the "
            "periodic table from Magnesium up to Uranium, even to heavier elements depending on the "
            "calibration of the instrument. This device has already been used to assess element content from "
            "Wallonia soil to more remote areas such as Siberia and Alaska (permafrost region). While "
            "laboratory standard methods can be quite expensive and time-consuming, the pXRF device offers a "
            "faster and cheaper method, and can also perform in situ measurement. Using this device on Mars "
            "would avoid having to bring back any sample on Earth and measurements would be directly stored "
            "on onboard computers."
        ),
    },
    # ---------------------------------------------------------------
    # Crew 212 — 2019
    # ---------------------------------------------------------------
    {
        "title": "Fully autonomous 3D mapping",
        "authors": "Crew 212",
        "year": "2019",
        "crew": "Crew 212",
        "category": "tech",
        "disciplines": ["Engineering", "Mapping", "Drones"],
        "description": (
            "We plan to improve the usability and efficiency of drone 3D mapping to the next level. The "
            "first step will be to gather data and software used by our predecessor Bastien Baix from the "
            "UCL to Mars 2018 mission. Mapping techniques are constantly evolving and updating the software "
            "behind the project is necessary.\n\n"
            "The core idea will be to automate the procedure itself. The precision of the built-in GPS "
            "positioning system (an error margin of 1-2 meters) and the camera should be enough to fully "
            "automate the gathering and treatment of mapping data. UCL to Mars already owns a Parrot Bebop 2 "
            "drone that was bought by the previous crew for last year's experiments that we intend to reuse, "
            "and existing technologies can be used to create and share 3D paths around the MDRS.\n\n"
            "The challenge will be to optimize the paths every day, test the functionalities and find the "
            "easiest, fastest way to get updated data on site. This will require work before the mission for "
            "development and during it for optimization and continuous testing. The final goal would be to "
            "develop and test a powerful tool for 3D mapping in a desert environment that is complete, "
            "robust and easy to use even for non-engineers."
        ),
    },
    {
        "title": "Devices of interest tracking with Ultra-Wide Band geolocation system",
        "authors": "Simon Collignon",
        "year": "2019",
        "crew": "Crew 212",
        "category": "tech",
        "disciplines": ["Electronics", "Geolocation"],
        "description": (
            "Here on Earth, GPS technology brought various tools to our society in a wide tech area. Up "
            "there on Mars, it might be useful to implement GPS-like devices and keep track of what's going "
            "on in our new Martian civilization. Nowadays, there are different geolocation technologies for "
            "different purposes. In regard of the relatively small size of our facilities and the precise "
            "experiments undertaken, the most relevant setup is the one which maximizes accuracy at the "
            "expense of the detection range. Using this configuration, we will be able to monitor near EVA, "
            "conducted by our astronauts and rovers."
        ),
    },
    {
        "title": "Deployment of a swarm of Cube Lands",
        "authors": "Carl-Henrik Dahlqvist",
        "year": "2019",
        "crew": "Crew 212",
        "category": "tech",
        "disciplines": ["Engineering", "Electronics", "Networking"],
        "description": (
            "Mars presents a dynamic environment that cannot be fully described by measures taken by a small "
            "number of probes. However, current Martian missions are very costly and do not allow them to "
            "cover large regions of its surface. To get a more comprehensive view of Mars climate evolution, "
            "we propose to rely on miniaturized landers, called Cube Lands that could be deployed on large "
            "strands of Mars surface via drones. Those landers will include several scientific instruments "
            "such as a thermometer, light/radiation, pressure, CO2, wind or magnetic field sensor to "
            "characterize the environment and provide new insights into its evolution.\n\n"
            "In contrast with CubeSats, which could deploy large solar panels and antennas, Cube Lands are "
            "affected by the planet's gravity. Therefore, we propose to rely on ultra-low power RF "
            "transceiver to reduce power consumption and be able to use a single solar panel covering one of "
            "the Cube Land sides. However, such transceivers have a much lower range which implies that Cube "
            "Lands could only communicate with nearest neighbors. A transmission algorithm will therefore be "
            "included in each lander to transmit, via the Cube Lands network, their information to the "
            "deployment unit which in turn could transfer the set of data to the Earth. The concept will be "
            "tested at the MDRS via the deployment of a dozen landers via a drone. The electronic system "
            "will be based on the Arduino platform and includes sensors, a solar panel, a charging unit, a "
            "battery for data collection during the night and a transceiver for data transmission to the "
            "main unit via the landers network."
        ),
    },
    {
        "title": "Enhancing leguminous plant nutrition via mycorrhiza symbiosis in a Martian simulated environment",
        "authors": "Chloé Peduzzi",
        "year": "2019",
        "crew": "Crew 212",
        "category": "health",
        "disciplines": ["Biology", "Botany"],
        "description": (
            "As a one-way trip to Mars is estimated at 6 months at the shortest, a round-trip mission to the "
            "red planet could last years. Therefore, setting up technologies to grow food in complete "
            "autonomy seems crucial. One main issue remains enhancing plant nutrition and increasing their "
            "resistance to stress and drought.\n\n"
            "To elucidate that point, we propose to study beneficial mycorrhizal fungi connecting with plant "
            "roots and forming a network of fungal fibres, bringing water and nutrients to the plant. They "
            "support the plant for its entire life and improve yield.\n\n"
            "On the one hand, we will study how this network develops in a Martian simulated soil. On the "
            "other hand, we will measure the effectiveness of the symbiosis with a leguminous plant in such "
            "conditions. Through this research, we aim to expand scientific knowledge on how Martian "
            "conditions affect symbiotic relationships between terrestrial organisms."
        ),
    },
    {
        "title": "Spirulina as space food",
        "authors": "Chloé Peduzzi",
        "year": "2019",
        "crew": "Crew 212",
        "category": "health",
        "disciplines": ["Biology", "Nutrition"],
        "description": (
            "As water is a limiting factor on Mars, lots of questions related to how to grow food on the Red "
            "Planet remain unsolved. On this purpose, current scientific research focuses on developing "
            "technologies to grow highly nutritive food requiring small amount of water. One possible option "
            "is spirulina! Indeed, those cyanobacteria are highly prospective for astronauts' alimentation "
            "during future Martian explorations. Not only can it be taken as a dietary supplement enriched "
            "in proteins, but it has also therapeutic properties.\n\n"
            "In that sense, we propose to establish a spirulina culture during our mission. The experiment "
            "will study the effect of space mission conditions on the culture system, including the small "
            "amount of space, materials and water available, the monitoring of the system and finally "
            "considering alternatives to improve the culture in such conditions."
        ),
    },
    {
        "title": "Martian Constitution",
        "authors": "Nathan Pechon",
        "year": "2019",
        "crew": "Crew 212",
        "category": "other",
        "disciplines": ["Law", "Political science"],
        "description": (
            "The research will consist of drafting a Martian constitution. Currently, no rules or "
            "legislation apply to Mars. However, law is essential to organize human society, especially as "
            "Martian missions are set to develop.\n\n"
            "The constitution will be drafted in collaboration with the crew, as such an important text "
            "should incorporate diverse opinions to be as democratic as possible. Nevertheless, he will play "
            "a central role in this process. His plan is to write articles and present them to the crew for "
            "voting. Naturally, he will consider the crew's opinions and appreciate every idea they "
            "contribute. The ultimate goal is to produce a coherent text that can be applied to future "
            "Martian missions."
        ),
    },
    {
        "title": "Impact of a Martian lifestyle on sleep quality",
        "authors": "Benjamin Flasse",
        "year": "2019",
        "crew": "Crew 212",
        "category": "health",
        "disciplines": ["Medicine", "Sleep research"],
        "description": (
            "A correct and regular sleep is essential for the recuperative power of the crew. For a long-term "
            "mission, recuperative power is crucial for the preservation of the reflexes and the cognitive "
            "functions of the members of the crew.\n\n"
            "The conditions of such a mission, which are among others confinement, the seclusion and the "
            "closeness with the team 24 hours a day, could have a serious impact on the quality of the sleep "
            "of the members of the team.\n\n"
            "This is why we will analyze the quality of sleep through complete polysomnography, actimetry, "
            "critical flicker fusion frequency and neuropsychometric tests."
        ),
    },
    {
        "title": "Simultaneous location and mapping algorithm using a depth camera",
        "authors": "Julien Amalaberque",
        "year": "2019",
        "crew": "Crew 212",
        "category": "tech",
        "disciplines": ["Computer science", "Robotics"],
        "description": (
            "On Mars, the lack of a global positioning system and the unreliability of the magnetic north "
            "means that other solutions need to be found to provide positioning and orientation. To do this "
            "for our drones, rovers and EVA suits, we decided to use an innovative algorithm called "
            "Simultaneous Location And Mapping, also already used with autonomous cars, with a depth camera "
            "(Intel RealSense D435i, released earlier this year). The basis used was RTAB-Map, an open-source "
            "implementation of the algorithm maintained by the University of Sherbrooke (Quebec, Canada). It "
            "works by creating a cloud of 3D points by extracting features from the image, and then by "
            "statistically computing the difference in position from the previous result.\n\n"
            "The first step needed to be tweaked in order to allow feature extraction to work on a red, "
            "deserted environment which is very different from the classic urban use cases usually described "
            "in literature.\n\n"
            "Once this was working well, another problem was that computing differences in position between "
            "images is an intensive task for a computer. Different image resolutions and frame-per-second "
            "settings had to be thoroughly tested to guarantee a reliable service. As a conclusion, the "
            "algorithm and the camera now work very well both inside the station and outside in the field. "
            "Its positioning ability can be used to automate the movements of any kind of unmanned vehicle "
            "or as a tool for astronauts."
        ),
    },
    {
        "title": "Development of a telescope for cosmic muon flux and density measurements",
        "authors": "Maxime Bernard",
        "year": "2019",
        "crew": "Crew 212",
        "category": "science",
        "disciplines": ["Physics", "Instrumentation"],
        "description": (
            "This project is based on the upgrading of a compact telescope based on small and gastight Glass "
            "Resistive Gas Chambers (\"minigRPC\") built last year by Sophie Wuyckens and is aimed at "
            "performing a feasibility study of possible research on Mars geology. The first part of the "
            "project will be an improvement of the software used to collect and analyze data. The second "
            "part will be the eventual refinements we could perform on different parts of the detector to "
            "make sure the data we get are the most reliable possible. The third part will consist of the "
            "collection of in-field data at the MDRS, and its analysis. The goal will then be to make a "
            "study of the muon flux generated by interactions of primary cosmic rays and, if time allows, to "
            "proceed to a radiography or tomography (3D) of the landscape (mountains, hills, etc.) of the "
            "Utah desert with \"muography\". This technique is very interesting for planets exploration. For "
            "instance, we could radiograph Mars and characterize its interior and know about the planet's "
            "evolutionary state and history as well as even finding some places geologically well-adapted "
            "places for future colony implantation."
        ),
    },
    {
        "title": "Study of Brownian motion of colloidal particles",
        "authors": "Eléonore Lieffrig",
        "year": "2019",
        "crew": "Crew 212",
        "category": "science",
        "disciplines": ["Physics", "Physical chemistry"],
        "description": (
            "The Brownian motion of colloidal particles is the motion of tiny particles in a fluid at rest. "
            "Several experiments regarding that field are currently running in the International Space "
            "Station, which offers the unique property of microgravity. The interest in studying the "
            "behavior of colloidal particles is that it finds applications in sectors such as environmental "
            "sciences, petrochemistry, chemistry and so on, including daily life. For example, we could be "
            "able to create a kind of plastics with better possibilities of recycling, or, a bit funnier, a "
            "vinaigrette that we would never have to shake for the components to be blended.\n\n"
            "We first built hermetic enclosures containing colloidal particles in water. The chosen colloids "
            "had the property to absorb light at 540 nm and reemit it at 560 nm. Therefore, a fluorescence "
            "microscopy technology allowed us to observe the reemitted light by placing a camera on the "
            "trajectory of the beam. That way, we were able to get the course of many particles on camera "
            "and then track them one by one to verify certain properties we were expecting. For example, the "
            "motion of the colloids is independent with regards to gravity and the position distribution "
            "around the initial point is a gaussian curve.\n\n"
            "Regarding the Musk observatory, the sun was very calm during our rotation, but we could observe "
            "little prominences on SOL 3. It was such a great opportunity to use this telescope."
        ),
    },
    # ---------------------------------------------------------------
    # Crew 190 — 2018
    # ---------------------------------------------------------------
    {
        "title": "Spirulina as a food solution for astronauts",
        "authors": "Maximilien Richald",
        "year": "2018",
        "crew": "Crew 190",
        "category": "health",
        "disciplines": ["Biology", "Nutrition"],
        "description": (
            "An astronaut eats one kilogram of food, breathes one kilogram of oxygen and drinks three liters "
            "of water. Astronauts also produce waste, mainly water. During long-term space mission, it is "
            "impossible to carry as much food and water for reasons of costs and logistics. Let's recycle! "
            "The MELiSSA project (Micro-Ecological Life Support System Alternative) focuses on means to "
            "enable long-term space missions. Using microorganisms such as Spirulina, bioreactors transform "
            "organic and non-organic waste into water, food and oxygen. Twenty-five years ago, the Belgian "
            "Nuclear Research Center (SCK•CEN) was at the base of the MELiSSA project. The European Space "
            "Agency (ESA) is now coordinating this large and international project. SCK•CEN studies the "
            "evolution of bacteria under the influence of radiations and weightlessness. In December 2017, "
            "the SPACEX-13 rocket took off from the Kennedy Space Center in Florida on its way to the "
            "International Space Station (ISS). On board was the very first photobioreactor containing "
            "Spirulina, developed by SCK•CEN in collaboration with ESA and the scientific consortium "
            "MELiSSA. During the UCL to Mars 2018 mission, researchers will study Spirulina in extreme "
            "conditions, at the Mars Desert Research Station. This cyanobacterium, intended to be used as a "
            "dietary supplement by astronauts, could have therapeutic properties on intestinal flora damaged "
            "by stress."
        ),
    },
    {
        "title": "Operation scheduling on MDRS under uncertainty: comparing classical and robust models",
        "authors": "Michael Saint-Guillain",
        "year": "2018",
        "crew": "Crew 190",
        "category": "science",
        "disciplines": ["Mathematics", "Operations research", "Computer science"],
        "description": (
            "We will consider the problem of scheduling a set of (experimental and logistic) operations in a "
            "constrained context such as the MDRS. When taking uncertainty into account while designing "
            "models, a robust solution that minimizes the probability of failure in the mission global "
            "objectives can be obtained.\n\n"
            "Based on real-life operations at MDRS, we will investigate different mathematical formulations "
            "for both deterministic and robust stochastic modeling of the problem, the latter taking "
            "uncertainty into account. To solve the deterministic problem, optimal and heuristic algorithms "
            "will be designed. Our principal goal is to show how the latter can be modified to take "
            "stochasticity into account while maximizing the probability of mission completion. Finally, "
            "computational experimentations will compare both approaches and highlight good practices for "
            "the benefit of future operation planning on Mars and in similar environments."
        ),
    },
    {
        "title": "The effect of hydrogel on the plant's growth in the GreenHab",
        "authors": "Frederic Peyrusson",
        "year": "2018",
        "crew": "Crew 190",
        "category": "health",
        "disciplines": ["Biology", "Botany"],
        "description": (
            "In the next long-duration exploration, plant systems will become essential components: the "
            "farther and longer humans go away from Earth, the greater the need to be able to grow plants "
            "for food and atmosphere recycling. Thus, we need robust and innovative plant systems which work "
            "in environments with limited equipment, space, water and suitable media for plant growth. Our "
            "MDRS mission aims at furthering already existing research, and we propose to study the effect "
            "of hydrogels on the plants' growth. Hydrogels are polymers absorbing large quantities of water "
            "and fixing seedling roots. Thus, they can considerably reduce plants' stress water loss and "
            "improve their growth and survival. Hydrogels will be tested in the context of reduced "
            "irrigation and using local soil powder, generally considered as less suitable for plant "
            "growth. Hydrogels could provide robust and innovative equipment to set up a Greenhouse, "
            "enhancing growth and quality and/or allowing the use of in situ loam from Martian soil powder "
            "to support good plant growth."
        ),
    },
    {
        "title": "Development of a telescope for cosmic muon flux and density measurements",
        "authors": "Sophie Wuyckens",
        "year": "2018",
        "crew": "Crew 190",
        "category": "science",
        "disciplines": ["Physics", "Instrumentation"],
        "description": (
            "This project is based on the building of a compact telescope based on small and gastight Glass "
            "Resistive Gas Chambers (\"minigRPC\") and is aimed at performing a feasibility study of possible "
            "research on Mars geology. The first part of the project will be a simulation optimizing "
            "parameters for the detector conception. The second part will be the construction of a miniRPC "
            "prototype with the ideal parameters taken from simulation, on which some tests will be "
            "performed. The third part will consist of the collection of in-field data at the MDRS, and its "
            "analysis. The goal will then be to make a study of the muon flux generated by interactions of "
            "primary cosmic rays and, if time allows, to proceed to a radiography or tomography (3D) of the "
            "landscape (mountains, hills, etc.) of the Utah desert with \"muography\". This technique is very "
            "interesting for planets exploration because, for example, we could radiograph Mars and "
            "characterize its interior and talk about the planet's evolutionary state and history as well as "
            "even finding some places geologically well-adapted places for future colony implantation."
        ),
    },
    {
        "title": "Construction of a vertical NFT hydroponics system in the MDRS",
        "authors": "Mario Sundic",
        "year": "2018",
        "crew": "Crew 190",
        "category": "health",
        "disciplines": ["Agronomy", "Hydroponics"],
        "description": (
            "A steady supply of food for the astronauts is one of the most fundamental requirements for any "
            "autonomous long-term space mission, such as an expedition to Mars. That food will almost "
            "exclusively be supplied by plants grown hydroponically in very tightly packed greenhouses, with "
            "very high exposure to different risk factors. It is therefore essential to evaluate how such a "
            "system evolves with and reacts to different stress stimuli, by testing it on Earth before "
            "departure.\n\n"
            "This experiment has two goals: firstly, the system, in the form of a vertical tower, will be "
            "built from the most basic materials available, emulating the process Martian astronauts would "
            "have to go through in case of a systems failure in which they would have to rebuild their food "
            "supply in restricted space and with restricted materials. Secondly, we will simulate the "
            "effects of extreme temperature variations, such as those which could potentially be encountered "
            "in a Martian setting, on different factors including plant growth, presence of pests, and "
            "nutrient degradation. This research will allow us to deepen our understanding of growth "
            "dynamics in the environment that is a space station and enhance the chances of success for "
            "future missions."
        ),
    },
    {
        "title": "Study of drug degradation at Mars Desert Research Station",
        "authors": "Martin Roumain",
        "year": "2018",
        "crew": "Crew 190",
        "category": "health",
        "disciplines": ["Pharmacology", "Chemistry"],
        "description": (
            "Medications degrade over time. Degradation of an active pharmaceutical ingredient (API) can "
            "result in reduced drug potency and increased toxicity due to the formation of degradation "
            "products. This degradation is accelerated by suboptimal storage conditions, as well as by some "
            "environmental factors of a Mars expedition such as microgravity, temperature variations and "
            "radiation, which may catalyze these drug alterations.\n\n"
            "With an expected duration of 6 to 7 months, a journey to Mars will most likely expose drugs to "
            "significant risk. It is then of paramount importance to study these risks and the accelerated "
            "degradation they provoke. A better understanding of this phenomenon will help to elaborate a "
            "specially designed space-grade packaging to ensure safety of acute and prolonged treatments to "
            "astronauts. During our mission we will study the degradation of a series of active "
            "pharmaceutical ingredients over time. We will quantify these molecules both in pure form and in "
            "tablets using UV-Vis spectroscopy and infrared spectroscopy."
        ),
    },
    {
        "title": "Martian bread: fermentation based on bacteria from human microbiota",
        "authors": "Ariane Sablon",
        "year": "2018",
        "crew": "Crew 190",
        "category": "health",
        "disciplines": ["Biology", "Food science"],
        "description": (
            "The Apollo 11 mission brought the first humans on the moon and back in 8 days 3 hours and 19 "
            "minutes. An inhabited mission to Mars will take years — the one-way trip is estimated at 6 "
            "months at the shortest. The organization of such a journey requires spectacular scientific and "
            "technological skills, including the transport of hundreds of tons of material and resources. "
            "The solution? A completely autonomous station including food level. We'll try to elucidate that "
            "point with this experiment dedicated to the making of Martian bread, more precisely a sourdough "
            "bread from ingredients directly produced in the station. The question of flour production, and "
            "thus cereal planting, is raised by our botanist Mario Sundic. The water, already present on the "
            "red planet in the form of ice, can be harvested and purified in consumable water. We will then "
            "attempt to produce bread through fermentation based on Lactobacillus isolated from our oral "
            "mucosa, and through fermentation with baking soda. If the experiment is successful, the only "
            "remaining issues will be the manufacturing of salt, and the high-temperature cooking of the "
            "bread..."
        ),
    },
    {
        "title": "Cartography with drones & MDRS drone monitoring",
        "authors": "Bastien Baix",
        "year": "2018",
        "crew": "Crew 190",
        "category": "tech",
        "disciplines": ["Geomatics", "Drones"],
        "description": (
            "The project involves the use of a drone in the field of geomatics for a mission at the MDRS. "
            "Establishing detailed and interactive mapping of the environment close to the station is a "
            "relevant objective. Indeed, carrying out efficient and secure missions is only made possible by "
            "studying the relief, the gradients and the zones of interest of the surface of Mars. The "
            "combined use of drone imaging and satellite imagery provides a complete mapping. This data will "
            "be processed digitally to obtain a complete map of the area surrounding the MDRS.\n\n"
            "The crew engineer function could be made more efficient by using drones. The crew engineer is "
            "responsible for the maintenance and integrity of the research station, and his/her function "
            "could be made more efficient by using drone. The objective of the project is to evaluate the "
            "utility of drones to access inaccessible areas and to take photographs to ensure the integrity "
            "of the base. We will analyze the feasibility of such a project in the difficult conditions of a "
            "space mission on Mars."
        ),
    },
    {
        "title": "Analysis of soil chemical composition",
        "authors": "Maximilien Richald",
        "year": "2018",
        "crew": "Crew 190",
        "category": "science",
        "disciplines": ["Geology", "Geochemistry", "Soil science"],
        "description": (
            "Bringing human life on a mission will be the first step of the Mars odyssey. Bringing humans to "
            "Mars is already a challenge, but keeping them alive is another one, and a much more complex "
            "one. To reach this objective, the humans who will live on the Red Planet will have to produce "
            "their own food most certainly by agriculture. Unfortunately, Martian soil is completely "
            "different from Earth's and the agriculture areas must be carefully chosen to avoid wasting "
            "seeds in a plantation doomed to death because of bad soil. This is why we propose to measure "
            "nitrogen, phosphorus and boron concentration to make sure that soil contains the required "
            "elements for growing crops. Nevertheless, physicochemical parameters are also highly decisive. "
            "To have better control of crop life and soil viability we will measure soil pH (acidity), but "
            "also soil electrical conductivity, which is related to ions concentration of various elements. "
            "By measuring all these parameters, we will provide strong knowledge of Mars soil composition "
            "which will facilitate agriculture on Martian soil."
        ),
    },
    {
        "title": "Biocompatibility of the simulated Martian environment for Terrestrial organism",
        "authors": "Frederic Peyrusson",
        "year": "2018",
        "crew": "Crew 190",
        "category": "health",
        "disciplines": ["Astrobiology", "Microbiology"],
        "description": (
            "Future long-duration space missions raise a lot of challenging questions. Can terrestrial "
            "organisms survive in a Mars environment, and what are the physical and chemical limits for "
            "Life? Biocompatibility of the Martian environment for terrestrial organisms is of particular "
            "interest for Astrobiology and space exploration.\n\n"
            "In that sense, we propose to study adaptation and survival strategies of microorganisms in a "
            "simulated Martian environment. This will imply the study of the ability of bacteria to produce "
            "and maintain spores and their mechanisms of adaptation to those unfavorable environments. This "
            "experiment could allow for the collection of precious information for biocompatibility of the "
            "Martian environment for Terrestrial organisms, establish a model for those studies, and figure "
            "out the probabilities and limitations for life to be distributed among planets of the Solar "
            "System."
        ),
    },
    {
        "title": "Impact of a Martian lifestyle on memory and reflexes",
        "authors": "Martin Roumain",
        "year": "2018",
        "crew": "Crew 190",
        "category": "health",
        "disciplines": ["Neuroscience", "Psychology"],
        "description": (
            "On Mars, several factors may have consequences on our organism such as the confinement, the "
            "change of scenery and the energy consumption spikes due to additional activity. These factors "
            "can induce fatigue and lead to decreased attention and memory performance, and increased "
            "reaction time. Being 225 million kilometers away from Earth, the crew will be on its own if "
            "something happens in the base. It is therefore very important to closely monitor the "
            "astronauts' physical condition during the whole expedition to Mars, which will probably last a "
            "couple of years. This is why we will then monitor the impact of this Martian lifestyle on "
            "memory and reflexes during our mission."
        ),
    },
    # ---------------------------------------------------------------
    # Crew 178 — 2017
    # ---------------------------------------------------------------
    {
        "title": "Telecommunication relays and marking risk areas",
        "authors": "Crew 178",
        "year": "2017",
        "crew": "Crew 178",
        "category": "tech",
        "disciplines": ["Telecommunications"],
        "description": (
            "How to communicate with crew members without satellites or magnetic field? How to map risk "
            "areas? This project proposes an original solution based on the use of telecommunication relays "
            "and sound beacons."
        ),
    },
    {
        "title": "Characterization of the environment by seismic refraction",
        "authors": "Crew 178",
        "year": "2017",
        "crew": "Crew 178",
        "category": "science",
        "disciplines": ["Geophysics", "Geology"],
        "description": (
            "Characterization of Martian subsurface under a geological and hydrogeological perspective is "
            "essential to understand the Martian environment. The objective of this project is to assess "
            "the interest of seismic refraction."
        ),
    },
    {
        "title": "Physiotherapeutic experiment about muscle wasting",
        "authors": "Crew 178",
        "year": "2017",
        "crew": "Crew 178",
        "category": "health",
        "disciplines": ["Physiotherapy", "Physiology"],
        "description": (
            "How to avoid degradation of the physical condition of a crewed mission to Mars? This project "
            "proposes to test the effectiveness of stress exercises and strength tests, coupled with the "
            "use of a cuff."
        ),
    },
    {
        "title": "Spectroscopy",
        "authors": "Crew 178",
        "year": "2017",
        "crew": "Crew 178",
        "category": "science",
        "disciplines": ["Astronomy", "Spectroscopy"],
        "description": (
            "Mars offers an ideal site to install an observatory! Indeed, with an atmosphere 100 times less "
            "thick, the data are not distorted. The spectroscopy experiment on Mars would be very "
            "interesting."
        ),
    },
    {
        "title": "Detection of muons",
        "authors": "Crew 178",
        "year": "2017",
        "crew": "Crew 178",
        "category": "science",
        "disciplines": ["Physics"],
        "description": (
            "The objective of this experiment is to detect muons under \"Martian conditions\", using a "
            "portable muon detector provided by the University of Louvain."
        ),
    },
    {
        "title": "Cartography and topometry around the base with drones",
        "authors": "Crew 178",
        "year": "2017",
        "crew": "Crew 178",
        "category": "tech",
        "disciplines": ["Geomatics", "Drones"],
        "description": (
            "Characterizing the area around the station using a drone is the subject of this ambitious "
            "project."
        ),
    },
    {
        "title": "Study of the renewal of oxygen by photosynthesis",
        "authors": "Crew 178",
        "year": "2017",
        "crew": "Crew 178",
        "category": "health",
        "disciplines": ["Biology", "Photosynthesis"],
        "description": (
            "The survival of a manned mission is only viable if resources renewal is possible. This "
            "experiment aims to test an oxygen-renewal process in a closed cycle."
        ),
    },
    {
        "title": "Characterization of the environment by X-Ray Diffraction",
        "authors": "Crew 178",
        "year": "2017",
        "crew": "Crew 178",
        "category": "science",
        "disciplines": ["Geology", "Mineralogy"],
        "description": (
            "Finding water on Mars is a major concern and a manned mission will certainly try confirming "
            "assumptions made by NASA. This project aims to characterize the hydrated rocks by X-ray "
            "diffraction."
        ),
    },
    # ---------------------------------------------------------------
    # Crew 166 — 2016
    # ---------------------------------------------------------------
    {
        "title": "Microbiology",
        "authors": "Crew 166",
        "year": "2016",
        "crew": "Crew 166",
        "category": "health",
        "disciplines": ["Microbiology", "Astrobiology"],
        "description": (
            "Our project is to design an experiment to find out any bacterial life in rocks from the Utah "
            "desert, to grow it in culture, and to characterize it by a range of phenotypic and biochemical "
            "tests applicable in Martian conditions. We should be able to run these tests with very few "
            "equipment. Given that a drilling project is not conceivable, we should just focus on surface "
            "rocks from various places, such as an old river's bed, to discover bacterial presence."
        ),
    },
    {
        "title": "3-D map conception & geologic simulation",
        "authors": "Crew 166",
        "year": "2016",
        "crew": "Crew 166",
        "category": "science",
        "disciplines": ["Geology", "Geomatics", "Simulation"],
        "description": (
            "The main idea of the project is to conceive a computer simulation of the land relief around the "
            "research station. Such a map would help the users to have a better knowledge of the "
            "surrounding terrain and thus allow them to plan the routes more easily, maximizing the "
            "available outdoors time to take measures or do experiments. As second part of the project, "
            "we'd like to add to this map the main characteristics of the surrounding rocks and soils. We "
            "would split the area into two parts: the zones which have already been studied before, for "
            "which we might find available data to build our geological simulation, and the non-previously "
            "studied areas. Concerning those areas, we'd first look up theoretical characteristics, "
            "assuming we roughly know what kind of soils we'll find and would then compare them to the "
            "characteristics which shall be measured in situ. Furthermore, another goal of this project "
            "would be to determine whether an area is dangerous or not, since flash floods or sand "
            "tornadoes may arise. The 3-D map would find a practicable route back to the station, using a "
            "vehicle or not. We also could work on another project, about radio operator relays and "
            "antennas, helping them to know whether an area is covered or not."
        ),
    },
    {
        "title": "Localization",
        "authors": "Crew 166",
        "year": "2016",
        "crew": "Crew 166",
        "category": "tech",
        "disciplines": ["Electronics", "Networking"],
        "description": (
            "During our simulation at the MDRS, we will be testing our danger zone detection system. The "
            "goal is to be able to warn the members of the team on EVA when they approach a dangerous zone. "
            "This experiment will be conducted with the other experiment of the Crew 166 (named 3D Map and "
            "Simulation). We will accomplish the detection of the dangerous zones using zigbee communication "
            "with small zigbee emitters and an Arduino card equipped with a zigbee to allow us to measure "
            "the distance to other modules. The zigbee modules have a RSSI entry (Received Signal Strength "
            "Indication), allowing us to know the distance to the emitter which will be at the entry of the "
            "danger zone. If the data are positive, the set-up can be used to allow the location of the "
            "members on EVA, by setting up a certain number of zigbee emitters in an area around the base. "
            "Then, by using a fingerprinting location method, a trilateration method or a triangulation "
            "method, we will be able to locate the members on EVA. The fingerprinting method will take more "
            "time to implement and is environment dependent (if the emitters are moved, the method is to be "
            "applied again), but will give better results."
        ),
    },
    {
        "title": "Using radio relay for communication",
        "authors": "Crew 166",
        "year": "2016",
        "crew": "Crew 166",
        "category": "tech",
        "disciplines": ["Telecommunications"],
        "description": (
            "The aim of this experiment is to test the use of a communication relay while on EVA. To do so, "
            "the team in EVA will place a relay on a good spot so they can use the radio at a greater "
            "distance. The relay is composed of two two-way handheld radios, and a repeater. This "
            "configuration is very cheap and power efficient, since the radios can work during the whole "
            "duration of the EVA. The relay will be placed at the top of a mast. The mast will have to be "
            "transported by the team and positioned while on EVA. Upon return from an EVA, the team will "
            "have to unmount the relay and take it back to the base. On \"Mars\" there is no such thing as "
            "cellphones. On the MDRS base in the Utah desert the participants will only be provided with a "
            "radio. The problem is that when there is an obstacle such as a hill or a canyon, communication "
            "is easily lost. Also, the team cannot go at a greater distance than the one the radio can "
            "cover. To improve communication, the team will use a portable radio relay that the team will "
            "place when they go on a mission. The distance at which communication is possible will be "
            "improved."
        ),
    },
    {
        "title": "Astronomy experiment",
        "authors": "Crew 166",
        "year": "2016",
        "crew": "Crew 166",
        "category": "science",
        "disciplines": ["Astronomy", "Spectroscopy"],
        "description": (
            "In the MUSK observatory, which belongs to the base, we will conduct a spectroscopy experiment. "
            "Spectroscopy is to analyze the light from celestial objects to know their composition. For "
            "this purpose, we will use an optical fiber to connect the telescope to the spectrometer that "
            "will be used for the measurements. A program will see the curve of the emission spectrum of "
            "the analyzed object. The data will be compared with the absorption lines of atoms and small "
            "molecules. We will conduct the first tests on the Moon and Jupiter and then we will look at "
            "the brightest stars visible this season and if it is high enough in the sky, we will try Mars "
            "and Saturn. Some of the stars expected to be observed are Sirius, Rigel, Procyon, Betelgeuse, "
            "Aldebaran, Capella, Pollux, Vega, Deneb, ... On Earth, the atmosphere will interact with the "
            "signal sent by astronomical object but on Mars the atmosphere is one hundred times less dense "
            "and will not interfere as much with the data. Furthermore, the MUSK observatory is equipped to "
            "make astrophotography, and it's planned to use this possibility. It allows us to have pictures "
            "of the object analyzed and other beauties present in the sky. The equipment needed is lent and "
            "funded by the Institute for Space Aeronomy."
        ),
    },
    # ---------------------------------------------------------------
    # Crew 153 — 2015
    # ---------------------------------------------------------------
    {
        "title": "Video Story",
        "authors": "Crew 153",
        "year": "2015",
        "crew": "Crew 153",
        "category": "other",
        "disciplines": ["Creative arts", "Storytelling"],
        "description": (
            "My project is to create, write and film a \"video-novel\" (text exploring the links and limits "
            "between the expression capacities of the novel and the video). The plot of the novel will "
            "stage scientists' daily life, which would have been sent by the ESA (European Space Agency) on "
            "the Mars planet to lead some experiences. Beyond the creative approach supported by this work, "
            "the \"video-novel\", once achieved, could provide an exceptional showcase for the Mars Society: "
            "the potential readers will discover, through the novel, the functioning of the base and get a "
            "few glimpses of the life on the site."
        ),
    },
    {
        "title": "Microbiology",
        "authors": "Crew 153",
        "year": "2015",
        "crew": "Crew 153",
        "category": "health",
        "disciplines": ["Microbiology", "Astrobiology"],
        "description": (
            "Our project is to design an experiment to find out any bacterial life in rocks from the Utah "
            "desert, to grow it in culture, and to characterize it by a range of phenotypic and biochemical "
            "tests applicable in Martian conditions. We should be able to run these tests with very few "
            "equipment. Given that a drilling project is not conceivable, we should just focus on surface "
            "rocks from various places, such as an old river's bed, to discover bacterial presence."
        ),
    },
    {
        "title": "Streambed analysis",
        "authors": "Crew 153",
        "year": "2015",
        "crew": "Crew 153",
        "category": "science",
        "disciplines": ["Geology", "Hydrology"],
        "description": (
            "The previous crews from UCL (crew 127 and 136) began a project with the objective of "
            "establishing a model of the past flow for a dry stream as the conditions would be close to the "
            "ones encountered on Mars and could provide interesting observations. Encouraging results were "
            "found last year and publication on this subject has been made. This year, we plan to improve "
            "the results by working in three different directions: establishing the regime of the river, "
            "doing a sediment transport model and finally completing the result by making a statistical "
            "analysis instead of a deterministic study."
        ),
    },
    {
        "title": "Astrophysics",
        "authors": "Crew 153",
        "year": "2015",
        "crew": "Crew 153",
        "category": "science",
        "disciplines": ["Astrophysics", "Astronomy"],
        "description": (
            "This involves detecting celestial objects located outside the Milky Way to measure their "
            "redshift (i.e., the redshift of the object's frequency spectrum due to the expansion of the "
            "universe). To achieve this, the experimental setup involves coupling a CCD spectroscope to the "
            "MDRS telescope.\n\n"
            "Using this setup, we will first be able to determine whether the object being observed is "
            "moving away from or toward us. This is a didactic method for illustrating the expansion of the "
            "universe. After that, we will be able to make more precise measurements of the spectra of "
            "objects moving away from us to determine their redshifts by comparing the spectra obtained "
            "with theoretical spectra. With these measurements, we will be able to determine the velocity "
            "and therefore the distance-luminosity (a measure of distance) between Earth and the object "
            "studied using Hubble's law."
        ),
    },
    {
        "title": "Geophysics",
        "authors": "Crew 153",
        "year": "2015",
        "crew": "Crew 153",
        "category": "science",
        "disciplines": ["Geophysics", "Geology"],
        "description": (
            "We know for sure that Mars had a magnetic field: satellites have detected a residual field "
            "induced by the rocks of its crust. Therefore, we wish to carry out an experiment about the "
            "magnetic properties of rocks in the Utah desert. The goal would be to determine as much as "
            "possible about the magnetic field that existed back when the rock was formed."
        ),
    },
    {
        "title": "Communication signal mapping",
        "authors": "Crew 153",
        "year": "2015",
        "crew": "Crew 153",
        "category": "science",
        "disciplines": ["Astrophysics", "Astronomy"],
        "description": (
            "The experiment consists in detecting galaxies out of the Milky Way to measure their spectral "
            "redshift in Mars analog conditions. To do that, we will couple a spectroscope CCD to the "
            "telescope of the MDRS. Thanks to this, we will be able to determine if the observed objects are "
            "moving away or closer. It is a didactic method to illustrate the expansion of the Universe. "
            "Then we will make more precise measures of the spectrum of objects moving away to determine "
            "their red shift. With these measures, we will be able to determine the speed and then the "
            "distance-luminosity of the object thanks to the Hubble law."
        ),
    },
    # ---------------------------------------------------------------
    # Crew 136 — 2014
    # ---------------------------------------------------------------
    {
        "title": "Streambed analysis",
        "authors": "Crew 136",
        "year": "2014",
        "crew": "Crew 136",
        "category": "science",
        "disciplines": ["Geology", "Hydrology"],
        "description": (
            "The previous crew from UCL (crew 127) began a project with the objective of establishing a "
            "model of the past flow for a dry streambed as the conditions would be close to the ones "
            "encountered on Mars and could provide interesting observations. We plan to continue and "
            "develop this project. The project ended with a mapping of the studied area and an estimation "
            "of the past flow. We want to go further with the data collecting and the model obtained last "
            "year. By using more parameters and more accurate data, the objective would be to determine "
            "the infiltration proportion and characteristics of the flow such as discharge and duration. "
            "Those additional parameters would be the nature of the soil, the size and volume of "
            "sediments, the shape of the bed, etc. They would be implemented with a MATLAB program to "
            "obtain a coherent model of the flow and its origin. By analyzing the duration and discharge, "
            "we could obtain a global estimation of the water transiting by this bed over a longer period. "
            "The final objective would be a 3D mapping of the bed and its characteristics: volume, speed "
            "and infiltration."
        ),
    },
    {
        "title": "Altitude measurements",
        "authors": "Crew 136",
        "year": "2014",
        "crew": "Crew 136",
        "category": "science",
        "disciplines": ["Meteorology", "Instrumentation"],
        "description": (
            "The project aims to retrieve meteorological data via a helium balloon. Our sensors will record "
            "the temperature, the humidity, the wind velocity, the pressure and the QNH or even the dew "
            "point. This data will be extrapolated to draw a model with respect to the altitude, to process "
            "a weather forecast. The protocol will be generalized to evaluate the feasibility of this "
            "experiment in real situation: on Mars."
        ),
    },
    {
        "title": "Geological prospection with UV",
        "authors": "Crew 136",
        "year": "2014",
        "crew": "Crew 136",
        "category": "science",
        "disciplines": ["Geology", "Geochemistry"],
        "description": (
            "The purpose of the project is to find the presence of ancient water channels in desert. The "
            "methodology consists in finding a place that we assume to be a dry channel. The evaporite "
            "minerals (halite, gypsum, etc.) have the capacity to fluoresce when they are lighted by "
            "ultraviolet waves (long and short). The procedure will consist of collecting samples of "
            "minerals along the dry channel and to reference and localize all of them with the GPS. The "
            "second part of the study will be the lighting of the sample with the UV light and test the "
            "minerals with hydrochloric acid (HCl) (for the carbonates). When the samples are referenced as "
            "evaporitic or not, they are put on a map with the software ArcMap from the ESRI suite, "
            "ArcGIS. The result will be a map with all the samples which will delimit the rivers. With "
            "these results it will be possible to set up the presence of an ancient river."
        ),
    },
    {
        "title": "Observation and spectral analysis of planets",
        "authors": "Crew 136",
        "year": "2014",
        "crew": "Crew 136",
        "category": "science",
        "disciplines": ["Astronomy", "Spectroscopy"],
        "description": (
            "The location of Mars and the fact that it does not have magnetic fields or atmosphere make it "
            "the perfect spot to observe our solar system. We will thus make use of the Musk Observatory "
            "and optic spectrometers to proceed with measurements of the spectrum emitted by planets from "
            "our solar system. Once the spectrum is recorded, we'll analyze it and will be able to "
            "determine the atmospheric composition of the observed object. We will also employ the "
            "telescope to take pictures of planets and other celestial bodies. There will be two supernovas "
            "that have recently exploded and that will be fully visible!"
        ),
    },
    # ---------------------------------------------------------------
    # Crew 127 — 2013
    # ---------------------------------------------------------------
    {
        "title": "Local positioning system for mars",
        "authors": "Crew 127",
        "year": "2013",
        "crew": "Crew 127",
        "category": "tech",
        "disciplines": ["Electronics", "Positioning systems"],
        "description": (
            "Once mankind starts to explore Mars, they will need to know their position on the planet. "
            "Since there will be no GPS at first, they will need to use a different positioning system. We "
            "thought of using triangulation to solve this problem. We will use fixed beacons made of "
            "Arduino chips with known positions and movable beacons that will be carried by the crew. By "
            "analyzing the power of the signal received by the movable beacons and their information, the "
            "crew can know its position. One advantage of this approach would be the fact that the "
            "exploring crew could extend the beacon network with its advance in unknown territory. It "
            "could also be used to carry information from the field to the headquarters.\n\n"
            "This project would be an improvement of a project started by Crew 103 that failed due to "
            "hardware issues. We plan to use their previous experience and equipment, which will help us "
            "to achieve the first results even faster and give us more time to improve the project."
        ),
    },
    {
        "title": "Observation of astronomical objects from mars",
        "authors": "Crew 127",
        "year": "2013",
        "crew": "Crew 127",
        "category": "science",
        "disciplines": ["Astronomy", "Astrophysics"],
        "description": (
            "Mars has a very tiny atmosphere compared to the Earth, so telescopes located on Martian soil "
            "would be more efficient because of the absence of atmospheric perturbations. Another big "
            "advantage to being on Mars (or equivalent to the desert of Utah) is that there is no luminous "
            "pollution, which becomes a chronic problem on Earth.\n\n"
            "We plan to observe the sky between 10 pm and 3 am because we want to observe all the objects "
            "before appearing in the vision field. So at the MDRS we will use the MUSK observatory, and the "
            "software \"stellarium\" on windows. It will help us to locate astronomical objects. We'll "
            "follow the training on the website to become experts in that field and to be able to use the "
            "CCD camera and the different filters for photography."
        ),
    },
    {
        "title": "A study of the past climatic conditions through rock and sediment analysis",
        "authors": "Crew 127",
        "year": "2013",
        "crew": "Crew 127",
        "category": "science",
        "disciplines": ["Geology", "Sedimentology"],
        "description": (
            "The geology of Mars holds important information on the previous climatic conditions of the "
            "planet. The main goal of this project is to analyze the nature of the rocks around the MDRS to "
            "determine these conditions and to produce a satisfying model of their formation. As the "
            "surface of Mars is now mainly dry, the wind is the only cause of erosion, and the observation "
            "of the sediments should provide enough data to estimate the atmospheric conditions and "
            "dominant winds. A global mapping of the rocks localization according to their nature is "
            "planned to reconstruct the past landscape and obtain a global model of the wind directions "
            "and sedimentation around the station."
        ),
    },
    {
        "title": "A search of water traces by erosion analysis",
        "authors": "Crew 127",
        "year": "2013",
        "crew": "Crew 127",
        "category": "science",
        "disciplines": ["Geology", "Geomorphology"],
        "description": (
            "The observations on Mars show landscape structures like water flow environments on Earth and "
            "the Curiosity rover has recently found rocks characteristic of stream beds. However, the "
            "surface of Mars is now completely dry, and the landscape and sediments are the last "
            "indicators of past water traces. This project is centered on the observation of the landscape "
            "and the analysis of sedimentation and erosion around the MDRS. His main objective is to "
            "determine the respective part of water flow and wind erosion in the formation of the local "
            "geographic structures. In case a typical stream bed is found, the sedimentation structure and "
            "erosion will be considered to establish a model of the past water flow and its influence on "
            "the landscape."
        ),
    },
    {
        "title": "Desensitization of the smell in close space in terms of time",
        "authors": "Crew 127",
        "year": "2013",
        "crew": "Crew 127",
        "category": "health",
        "disciplines": ["Physiology", "Sensory science"],
        "description": (
            "Astronauts on missions on Mars will stay in closed areas for quite a long time. So, the idea "
            "of this project is to study the possible impact of such living conditions on the smell's "
            "ability of the crew members, that is the bluntness of their sense. It can be due to numerous "
            "factors like dust in the living area, the absence of usual and common smells, and so on. This "
            "could create an insecure climate in the station because the astronauts would become less "
            "sensitive to smoke smells or toxic gas, for example, which could threaten the whole team. To "
            "do so, on the first day of our simulation members will be educated to recognize the smells "
            "that we have brought with us in the form of essential oils. Then after a week the first group "
            "will take a test which will consist in distinguishing the different smells of a mixing. "
            "Finally, at the end of our simulation the second group will take it also. By comparing both "
            "results we will be able to determine if bluntness really occurs."
        ),
    },
]
