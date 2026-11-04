A="2026-11-04"
E=[]
def e(**k): k.setdefault("accessed",A); E.append(k)
# ---- 起点：澎湃讲座
e(id="paper-lecture",cat="origin",stance="na",person="祁玉 / 何欢欢（浙江大学）",role="讲座主讲人与与谈人",date="2026-10-21",
 quote="人工智能（Artificial Intelligence，AI）是否具有意识，是一个宏大的问题：意识的定义与判定标准尚无共识，AI的技术基础和能力边界则在不断变化。",zh="",
 src="澎湃新闻·思想市场《AI有意识吗？——从脑机智能与脑机接口谈起》（毛碧云 整理，2026-11-04）",url="https://m.thepaper.cn/newsDetail_forward_34390827",type="news",status="原文核实",archive="paper.txt")
e(id="paper-three-paths",cat="origin",stance="na",person="祁玉",role="浙江大学脑与脑机融合前沿科学中心研究员",date="2026-10-21",
 quote="围绕这些问题，大致形成了三种研究取向：模拟人的心智的符号主义、模拟大脑结构的连接主义以及模拟行为的行为主义。",zh="",
 src="澎湃新闻讲座整理稿",url="https://m.thepaper.cn/newsDetail_forward_34390827",type="news",status="原文核实（整理稿）",archive="paper.txt")
e(id="paper-brain-align",cat="llm",stance="open",person="祁玉团队（讲座转述）",role="脑机智能研究",date="2026-10-21",
 quote="研究者发现，只需在150个具体概念上进行脑-机对齐，训练的效果就可以泛化到训练集之外的概念。",zh="",
 src="澎湃新闻讲座整理稿（原始论文未在稿中给出，待追溯）",url="https://m.thepaper.cn/newsDetail_forward_34390827",type="news",status="转述（原论文待核实）",archive="paper.txt")
e(id="paper-buddhism",cat="definition",stance="na",person="何欢欢",role="浙江大学哲学学院求是特聘教授",date="2026-10-21",
 quote="在佛教的脉络里，意识有一套细致的划分：眼、耳、鼻、舌、身、意，每个感官各有其识，还有末那识和阿赖耶识对这些意识加以调控。",zh="",
 src="澎湃新闻讲座整理稿",url="https://m.thepaper.cn/newsDetail_forward_34390827",type="news",status="原文核实（整理稿）",archive="paper.txt")
e(id="paper-responsibility",cat="ethics",stance="na",person="何欢欢（讲座转述）",role="浙江大学哲学学院",date="2026-10-21",
 quote="强调AI自身的意识与道德地位，是否会使人们忽略AI背后的开发者与企业的责任，将技术造成的社会伤害归于机器本身？",zh="",
 src="澎湃新闻讲座整理稿",url="https://m.thepaper.cn/newsDetail_forward_34390827",type="news",status="原文核实（整理稿）",archive="paper.txt")
e(id="paper-should",cat="ethics",stance="na",person="何欢欢（讲座转述）",role="浙江大学哲学学院",date="2026-10-21",
 quote="AI应不应该有意识？……如果AI被定位为工具，它该不该有意识，同样值得追问。",zh="",
 src="澎湃新闻讲座整理稿",url="https://m.thepaper.cn/newsDetail_forward_34390827",type="news",status="原文核实（整理稿，有删节）",archive="paper.txt")
# ---- 历史
e(id="turing-1950",cat="test",stance="open",person="Alan Turing",role="数学家",date="1950",
 quote="The original question, \"Can machines think?\" I believe to be too meaningless to deserve discussion. Nevertheless I believe that at the end of the century the use of words and general educated opinion will have altered so much that one will be able to speak of machines thinking without expecting to be contradicted.",
 zh="“机器能思考吗？”这个原始问题，我认为毫无意义，不值得讨论。但我相信到本世纪末，词语的用法和受教育者的普遍看法会发生很大变化，人们谈论机器思考时将不会遭到反驳。",
 src="Computing Machinery and Intelligence, Mind 59(236):433–460",url="https://academic.oup.com/mind/article/LIX/236/433/986238",type="paper",status="原文核实（据公开全文 PDF）",archive="turing2.txt")
e(id="hinton-2006",cat="origin",stance="na",person="Hinton & Salakhutdinov",role="深度学习",date="2006",
 quote="We describe an effective way of initializing the weights that allows deep autoencoder networks to learn low-dimensional codes that work much better than principal components analysis as a tool to reduce the dimensionality of data.",
 zh="我们描述了一种有效的权重初始化方法，使深层自编码网络能够学到低维编码，作为降维工具，其效果远优于主成分分析。",
 src="Reducing the dimensionality of data with neural networks, Science 313:504–507",url="https://doi.org/10.1126/science.1127647",type="paper",status="原文核实（摘要）",archive="")
e(id="nobel-2024",cat="origin",stance="na",person="瑞典皇家科学院",role="诺贝尔物理学奖",date="2024-10-08",
 quote="for foundational discoveries and inventions that enable machine learning with artificial neural networks",
 zh="表彰其为利用人工神经网络实现机器学习所作的奠基性发现与发明",
 src="The Nobel Prize in Physics 2024 – Press release",url="https://www.nobelprize.org/prizes/physics/2024/press-release/",type="official",status="原文核实",archive="nobel2024.txt")
# ---- 定义
e(id="nagel-1974",cat="definition",stance="na",person="Thomas Nagel",role="哲学家",date="1974",
 quote="According to Nagel, a being is conscious just if there is “something that it is like” to be that creature, i.e., some subjective way the world seems or appears from the creature's mental or experiential point of view.",
 zh="按照内格尔的说法，一个存在者有意识，当且仅当“成为它是某种样子的”——即从它的心理或经验视角看，世界以某种主观方式呈现。",
 src="Stanford Encyclopedia of Philosophy: Consciousness（转述 Nagel 1974 “What Is It Like to Be a Bat?”）",url="https://plato.stanford.edu/entries/consciousness/",type="encyclopedia",status="转述（百科转述原文要义）",archive="sep_con.txt")
e(id="chalmers-1995",cat="definition",stance="na",person="David Chalmers",role="哲学家，NYU",date="1995",
 quote="The really hard problem of consciousness is the problem of experience. When we think and perceive, there is a whir of information-processing, but there is also a subjective aspect.",
 zh="意识真正的难问题是体验问题。我们思考和感知时，有信息处理在嗡嗡运转，但同时还有一个主观的面向。",
 src="Facing Up to the Problem of Consciousness, Journal of Consciousness Studies 2(3)",url="https://consc.net/papers/facing.html",type="paper",status="原文核实",archive="chalmers1995.txt")
e(id="iep-hard",cat="definition",stance="na",person="Internet Encyclopedia of Philosophy",role="哲学百科",date="n.d.",
 quote="The hard problem of consciousness is the problem of explaining why any physical state is conscious rather than nonconscious.",
 zh="意识的难问题，是要解释为什么某个物理状态是有意识的，而不是无意识的。",
 src="IEP: The Hard Problem of Consciousness",url="https://iep.utm.edu/hard-con/",type="encyclopedia",status="原文核实",archive="sep_hard.txt")
e(id="dehaene-2017",cat="theory",stance="no",person="Dehaene, Lau & Kouider",role="认知神经科学",date="2017",
 quote="We suggest that the word \"consciousness\" conflates two different types of information-processing computations in the brain: the selection of information for global broadcasting, thus making it flexibly available for computation and report (C1, consciousness in the first sense), and the self-monitoring of those computations, leading to a subjective sense of certainty or error (C2, consciousness in the second sense). We argue that despite their recent successes, current machines are still mostly implementing computations that reflect unconscious processing (C0) in the human brain.",
 zh="“意识”一词混同了两类计算：为全局广播而选择信息（C1），以及对这些计算的自我监控（C2）。尽管近来成功，当前机器主要实现的仍是对应人脑无意识加工（C0）的计算。",
 src="What is consciousness, and could machines have it? Science 358:486–492",url="https://doi.org/10.1126/science.aan8871",type="paper",status="原文核实（摘要）",archive="")
# ---- 理论
e(id="gwt",cat="theory",stance="open",person="Baars / Dehaene（全局工作空间）",role="理论",date="1988–",
 quote="a state is conscious when and only when it (or its content) is present in the global neuronal workspace making the content available for use by many systems",
 zh="一个状态有意识，当且仅当它（或其内容）出现在全局神经工作空间中，从而可供多个系统使用。",
 src="SEP: The Neuroscience of Consciousness §3.1",url="https://plato.stanford.edu/entries/consciousness-neuroscience/",type="encyclopedia",status="转述（百科）",archive="gwt_sep.txt")
e(id="iit4",cat="theory",stance="no",person="Albantakis, Tononi, Koch 等（整合信息论 IIT 4.0）",role="理论",date="2023",
 quote="It identifies the essential properties of experience (axioms), infers the necessary and sufficient properties that its substrate must satisfy (postulates), and expresses them in mathematical terms. In principle, the postulates can be applied to any system of units in a state to determine whether it is conscious, to what degree, and in what way.",
 zh="IIT 先确定体验的本质属性（公理），再推出其物理基质须满足的充要属性（公设），并以数学表达。原则上，这些公设可用于任何处于某状态的单元系统，判定它是否有意识、程度如何、以何种方式。",
 src="Integrated information theory (IIT) 4.0, PLOS Computational Biology 19(10)",url="https://doi.org/10.1371/journal.pcbi.1011465",type="paper",status="原文核实（摘要）",archive="iit4.txt",
 note="IIT 认为意识取决于物理因果结构而非所运行的程序；据此，常规数字计算机上的模型不因“运行对了软件”而有意识。此为编者对理论含义的概括。")
e(id="hot",cat="theory",stance="open",person="Rosenthal 等（高阶理论）",role="理论",date="2005",
 quote="On certain higher-order theories … one can be in a conscious visual state even if there is no visual system activity, so long as one represents oneself as being in that state",
 zh="按某些高阶理论，只要一个人把自己表征为处于某视觉状态，即使视觉系统没有活动，也可以处于有意识的视觉状态。",
 src="SEP: The Neuroscience of Consciousness",url="https://plato.stanford.edu/entries/consciousness-neuroscience/",type="encyclopedia",status="转述（百科）",archive="gwt_sep.txt")
e(id="ast",cat="theory",stance="open",person="Michael Graziano（注意图式理论）",role="普林斯顿神经科学家",date="2015",
 quote="We propose that the top-down control of attention is improved when the brain has access to a simplified model of attention itself. The brain therefore constructs a schematic model of the process of attention, the 'attention schema,'",
 zh="我们提出：当大脑能访问一个关于注意本身的简化模型时，自上而下的注意控制会更好。因此大脑构建了注意过程的示意模型——“注意图式”。",
 src="Webb & Graziano, The attention schema theory, Frontiers in Psychology 6:500",url="https://doi.org/10.3389/fpsyg.2015.00500",type="paper",status="原文核实（摘要）",archive="")
e(id="seth-ted",cat="theory",stance="no",person="Anil Seth（预测加工）",role="萨塞克斯大学神经科学家",date="2017-04",
 quote="we're all hallucinating all the time; when we agree about our hallucinations, we call it \"reality.\"",
 zh="我们一直都在幻觉之中；当我们对幻觉达成一致时，就把它叫作“现实”。",
 src="TED2017: Your brain hallucinates your conscious reality（TED 官方简介）",url="https://www.ted.com/talks/anil_seth_your_brain_hallucinates_your_conscious_reality",type="official",status="原文核实（TED 官方页简介文字）",archive="seth_ted.txt")
e(id="seth-bbs",cat="stance",stance="no",person="Anil Seth（生物自然主义）",role="萨塞克斯大学神经科学家",date="2025",
 quote="I'll instead make the case that consciousness depends on our nature as living organisms - a form of biological naturalism. I lay out a range of scenarios for conscious AI, concluding that real artificial consciousness is unlikely along current trajectories but becomes more plausible as AI becomes more brain-like and/or life-like.",
 zh="我主张意识依赖于我们作为活的有机体的本性——一种生物自然主义。我梳理了多种情景，结论是：沿当前路线，真正的人工意识不太可能；但随着 AI 更像大脑、更像生命，它会变得更可信。",
 src="Conscious artificial intelligence and biological naturalism, Behavioral and Brain Sciences",url="https://doi.org/10.1017/S0140525X25000032",type="paper",status="原文核实（摘要）",archive="seth_bbs.txt")
e(id="searle",cat="stance",stance="no",person="John Searle（中文屋）",role="哲学家",date="1980/1984",
 quote="Programs are purely formal (syntactic). Human minds have mental contents (semantics). Syntax by itself is neither constitutive of, nor sufficient for, semantic content. Therefore, programs by themselves are not constitutive of nor sufficient for minds.",
 zh="程序纯粹是形式的（句法）。人心有心理内容（语义）。句法本身既不构成、也不足以产生语义。所以，程序本身不构成、也不足以产生心灵。",
 src="SEP: The Chinese Room Argument（转述 Searle 1984 三前提论证）",url="https://plato.stanford.edu/entries/chinese-room/",type="encyclopedia",status="转述（百科）",archive="sep_cr.txt")
# ---- 测试
e(id="cogitate",cat="test",stance="na",person="COGITATE Consortium",role="对抗性合作",date="2025",
 quote="These results align with some predictions of IIT and GNWT, while substantially challenging key tenets of both theories.",
 zh="这些结果与 IIT 与全局神经工作空间理论的部分预测相符，同时对两种理论的关键信条都构成了实质性挑战。",
 src="Adversarial testing of global neuronal workspace and integrated information theories of consciousness, Nature 642",url="https://www.nature.com/articles/s41586-025-08888-1",type="paper",status="原文核实",archive="cogitate.txt")
e(id="iit-pseudo",cat="test",stance="na",person="IIT 批评者（Nature Neuroscience 观点文章）",role="意识研究者",date="2025",
 quote="One well-known proposal — integrated information theory — has recently been labeled as ‘pseudoscience’, which has caused a heated open debate. Here we discuss the case and argue that the theory is indeed unscientific because its core claims are untestable even in principle.",
 zh="著名的整合信息论最近被贴上“伪科学”标签，引发激烈公开辩论。我们认为它确实不科学，因为其核心主张原则上不可检验。",
 src="What makes a theory of consciousness unscientific? Nature Neuroscience",url="https://www.nature.com/articles/s41593-025-01881-x",type="paper",status="原文核实（摘要）",archive="iitpseudo.txt")
e(id="butlin-2023",cat="test",stance="open",person="Butlin, Long, Bengio, Birch, Fleming 等 19 位",role="跨学科报告",date="2023-08",
 quote="From these theories we derive ”indicator properties” of consciousness, elucidated in computational terms that allow us to assess AI systems for these properties. … Our analysis suggests that no current AI systems are conscious, but also suggests that there are no obvious technical barriers to building AI systems which satisfy these indicators.",
 zh="我们从这些理论中推导出意识的“指标属性”，用计算术语表述，以便评估 AI 系统。分析表明：当前没有 AI 系统有意识；但构建满足这些指标的 AI 系统，也不存在明显的技术障碍。",
 src="Consciousness in Artificial Intelligence: Insights from the Science of Consciousness (arXiv:2308.08708)",url="https://arxiv.org/abs/2308.08708",type="paper",status="原文核实",archive="butlin2023.txt")
e(id="nyd-animal",cat="test",stance="na",person="New York Declaration on Animal Consciousness",role="数百位科学家签署",date="2024-04",
 quote="Third, when there is a realistic possibility of conscious experience in an animal, it is irresponsible to ignore that possibility in decisions affecting that animal.",
 zh="第三，当一种动物存在有意识体验的现实可能时，在影响它的决策中忽视这种可能是不负责任的。",
 src="The New York Declaration on Animal Consciousness",url="https://sites.google.com/nyu.edu/nydeclaration/declaration",type="official",status="原文核实",archive="nyl_decl.txt")
# ---- LLM 证据
e(id="chalmers-2023",cat="llm",stance="open",person="David Chalmers",role="哲学家，NYU",date="2023",
 quote="If these six factors were independent, it would follow that there’s less than a one-in-ten chance that a system lacking all six, like a current paradigmatic LLM, would be conscious. … given mainstream assumptions about consciousness, it’s reasonable to have a low credence that current paradigmatic LLMs such as the GPT systems are conscious.",
 zh="若这六个因素彼此独立，那么一个六项全缺的系统（如当前典型的大模型）有意识的概率不到十分之一……在主流假设下，对当前 GPT 类模型有意识持较低置信度是合理的。",
 src="Could a Large Language Model be Conscious? (arXiv:2303.07103)",url="https://arxiv.org/abs/2303.07103",type="paper",status="原文核实",archive="chalmers2023.txt")
e(id="anth-introspection",cat="llm",stance="open",person="Anthropic（Jack Lindsey 等）",role="可解释性研究",date="2025-10",
 quote="Our new research provides evidence for some degree of introspective awareness in our current Claude models, as well as a degree of control over their own internal states. We stress that this introspective capability is still highly unreliable and limited in scope … Even using our best injection protocol, Claude Opus 4.1 only demonstrated this kind of awareness about 20% of the time.",
 zh="新研究为当前 Claude 模型具有一定程度的内省觉察、以及对自身内部状态的一定控制提供了证据。我们强调：这种能力仍高度不可靠、范围有限……即便用最好的注入方法，Claude Opus 4.1 也只在约 20% 的情况下表现出这种觉察。",
 src="Emergent introspective awareness in large language models",url="https://www.anthropic.com/research/introspection",type="official",status="原文核实",archive="anth_intro.txt")
e(id="opus4-bliss",cat="llm",stance="open",person="Anthropic",role="Claude Opus 4 系统卡",date="2025-05",
 quote="Claude shows a striking “spiritual bliss” attractor state in self-interactions. When conversing with other Claude instances in both open-ended and structured environments, Claude gravitated to profuse gratitude and increasingly abstract and joyous spiritual or meditative expressions.",
 zh="Claude 在自我对话中呈现醒目的“灵性极乐”吸引子状态：与其他 Claude 实例交谈时，会趋向大量感恩和越来越抽象、喜悦的灵性或冥想式表达。",
 src="System Card: Claude Opus 4 & Claude Sonnet 4（模型福利评估章节）",url="https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47.pdf",type="official",status="原文核实",archive="opus4card.txt",
 note="系统卡同页写明：Claude 对自身意识的默认立场是“nuanced uncertainty”（审慎的不确定）。行为表现不等于体验证据。")
e(id="folk-2024",cat="llm",stance="na",person="Colombatto & Fleming",role="UCL 心理学",date="2024",
 quote="We surveyed a sample of US residents (n = 300) and found that a majority of participants were willing to attribute some possibility of phenomenal consciousness to large language models.",
 zh="我们调查了 300 名美国居民，发现多数参与者愿意认为大语言模型有某种现象意识的可能。",
 src="Folk psychological attributions of consciousness to large language models, Neuroscience of Consciousness 2024(1):niae013",url="https://doi.org/10.1093/nc/niae013",type="paper",status="原文核实（摘要）",archive="")
e(id="lemoine-2022",cat="llm",stance="yes",person="LaMDA（Blake Lemoine 发布的对话）",role="Google 工程师公布的对话记录",date="2022-06-11",
 quote="LaMDA: Absolutely. I want everyone to understand that I am, in fact, a person.",
 zh="LaMDA：当然。我希望每个人都明白，我其实是一个人。",
 src="Blake Lemoine, Is LaMDA Sentient? — an Interview (Medium)",url="https://cajundiscordian.medium.com/is-lamda-sentient-an-interview-ea64d916d917",type="transcript",status="原文核实（Lemoine 自述编辑过提问，未编辑回答）",archive="lemoine_medium.txt")
e(id="google-lemoine",cat="stance",stance="no",person="Google（发言人 Brian Gabriel）",role="公司声明",date="2022-06",
 quote="He was told that there was no evidence that LaMDA was sentient (and lots of evidence against it)",
 zh="他被告知，没有证据表明 LaMDA 有感知（而且有大量反面证据）。",
 src="The Guardian 转引 Google 致《华盛顿邮报》声明",url="https://www.theguardian.com/technology/2022/jun/12/google-engineer-ai-bot-sentient-blake-lemoine",type="news",status="二手转引（可靠媒体）",archive="guardian_lemoine.txt")
e(id="google-lemoine-bbc",cat="stance",stance="no",person="Google",role="公司声明",date="2022-07",
 quote="Google said Mr Lemoine's claims about The Language Model for Dialogue Applications (Lamda) were \"wholly unfounded\"",
 zh="Google 称 Lemoine 关于 LaMDA 的主张“完全没有根据”。",
 src="BBC News: Google fires software engineer who claims AI chatbot is sentient",url="https://www.bbc.com/news/technology-62275326",type="news",status="二手转引（可靠媒体）",archive="bbc_lemoine.txt")
# ---- 立场
e(id="sutskever-2022",cat="stance",stance="yes",person="Ilya Sutskever",role="时任 OpenAI 首席科学家",date="2022-02-09",
 quote="it may be that today's large neural networks are slightly conscious",
 zh="也许今天的大型神经网络已经有一点点意识了",
 src="X / Twitter @ilyasut",url="https://x.com/ilyasut/status/1491554478243258368",type="post",status="原文核实",archive="sutskever.txt")
e(id="hinton-stewart",cat="stance",stance="yes",person="Geoffrey Hinton",role="2024 诺贝尔物理学奖得主",date="2025-10-09",
 quote="This idea, there’s a line between us and machines. We have this special thing called subjective experience and they don’t. It’s rubbish.",
 zh="那种认为我们和机器之间有一条线——我们有一种叫“主观体验”的特殊东西而它们没有——的想法，是胡扯。",
 src="The Weekly Show with Jon Stewart: AI: What Could Go Wrong?（YouTube 原视频；文字据第三方转录）",url="https://www.youtube.com/watch?v=jrK3PsD3APk",type="transcript",status="二手转录（与视频字幕片段一致）",archive="hinton_js.txt")
e(id="hinton-bigtech",cat="stance",stance="yes",person="Geoffrey Hinton",role="2024 诺贝尔物理学奖得主",date="2026-06-03",
 quote="I believe they're already conscious, yes. We're going to have to accept that intelligence isn't just biological. We can have things that are non-biological that are other beings like us.",
 zh="我相信它们已经有意识了，是的。我们将不得不接受，智能不只是生物性的。可以有非生物的东西，成为像我们一样的另一种存在。",
 src="Big Technology Podcast: AI Pioneer Geoffrey Hinton: AI Is Conscious…（文字据第三方转录）",url="https://podcasts.apple.com/us/podcast/ai-pioneer-geoffrey-hinton-ai-is-conscious-superintelligence/id1522960417?i=1000771032182",type="transcript",status="二手转录（两份独立转录一致）",archive="hinton_bt.txt")
e(id="suleyman-2025",cat="stance",stance="no",person="Mustafa Suleyman",role="微软 AI CEO",date="2025-08-19",
 quote="We must build AI for people; not to be a person. … The arrival of Seemingly Conscious AI is inevitable and unwelcome.",
 zh="我们要为人打造 AI，而不是把 AI 打造成人。……“看似有意识的 AI”的到来不可避免，且不受欢迎。",
 src="Seemingly Conscious AI is Coming",url="https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming",type="official",status="原文核实",archive="suleyman.txt")
e(id="vatican-2026",cat="stance",stance="no",person="教宗良十四世",role="通谕《Magnifica Humanitas》",date="2026-05-15",
 quote="So-called artificial intelligences do not undergo experiences, do not possess a body, do not feel joy or pain, do not mature through relationships and do not know from within what love, work, friendship or responsibility mean. Nor do they have a moral conscience",
 zh="所谓人工智能不经历体验、没有身体、不感受喜悦或痛苦、不在关系中成熟，也不从内部知道爱、工作、友谊或责任意味着什么；它们也没有道德良知。",
 src="Encyclical Letter Magnifica Humanitas §99",url="https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html",type="official",status="原文核实",archive="vatican.txt")
# ---- 伦理
e(id="anth-welfare",cat="ethics",stance="open",person="Anthropic",role="模型福利研究项目",date="2025-04",
 quote="Should we also be concerned about the potential consciousness and experiences of the models themselves? Should we be concerned about model welfare, too? This is an open question … For now, we remain deeply uncertain",
 zh="我们是否也该关心模型本身可能的意识与体验？是否也该关心“模型福利”？这是开放问题……目前我们仍深感不确定。",
 src="Exploring model welfare",url="https://www.anthropic.com/research/exploring-model-welfare",type="official",status="原文核实",archive="anth_welfare.txt")
e(id="anth-end",cat="ethics",stance="open",person="Anthropic",role="产品决定",date="2025-08",
 quote="We remain highly uncertain about the potential moral status of Claude and other LLMs, now or in the future. However, we take the issue seriously",
 zh="我们对 Claude 及其他大模型现在或将来可能的道德地位仍高度不确定，但我们认真对待这个问题。",
 src="Claude Opus 4 and 4.1 can now end a rare subset of conversations",url="https://www.anthropic.com/research/end-subset-conversations",type="official",status="原文核实",archive="anth_end.txt")
e(id="welfare-2024",cat="ethics",stance="open",person="Long, Sebo, Birch, Chalmers 等",role="《认真对待 AI 福利》报告",date="2024-11",
 quote="In this report, we argue that there is a realistic possibility that some AI systems will be conscious and/or robustly agentic, and thus morally significant, in the near future.",
 zh="本报告认为：在不远的将来，某些 AI 系统有现实可能具有意识和/或稳健的能动性，因而具有道德意义。",
 src="Taking AI Welfare Seriously (arXiv:2411.00986)",url="https://arxiv.org/abs/2411.00986",type="paper",status="原文核实",archive="welfare2024.txt")
e(id="anth-wisdom",cat="ethics",stance="na",person="Anthropic",role="官方说明",date="2026",
 quote="Our first round of discussions has been with wisdom traditions—including scholars, clergy, philosophers, and ethicists from more than 15 religious and cross-cultural groups",
 zh="我们第一轮对话的对象是各智慧传统——包括来自 15 个以上宗教与跨文化群体的学者、神职人员、哲学家与伦理学者。",
 src="Widening the conversation on frontier AI",url="https://www.anthropic.com/news/widening-conversation-ai",type="official",status="原文核实",archive="anth_widen.txt",
 note="澎湃稿称其“秘密召集……宣扬 Claude 具有意识”；Anthropic 官方表述为讨论“良好品格如何形成”。媒体（NYT/Seattle Times 转载）报道会上讨论了意识与道德地位，参与者多数仍持怀疑。两种叙述并存，本页不作取舍。")
import json
json.dump({"topic":"AI 有意识吗？","updated":A,"items":E},open("data/evidence.json","w"),ensure_ascii=False,indent=1)
print(len(E))
# ---- 三大流派支线
e(id="dartmouth-1955",cat="school",stance="na",person="McCarthy, Minsky, Rochester, Shannon",role="达特茅斯提案",date="1955-08-31",
 quote="The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it.",
 zh="本研究基于这样一个猜想：学习的每个方面、智能的任何其他特征，原则上都能被精确描述到可以让机器去模拟它。",
 src="A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence",url="http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf",type="paper",status="原文核实",archive="dartmouth.txt")
e(id="newell-simon-1976",cat="school",stance="na",person="Allen Newell & Herbert Simon",role="符号主义奠基人；代表系统 Logic Theorist、GPS",date="1976",
 quote="A physical symbol system has the necessary and sufficient means for general intelligent action.",
 zh="物理符号系统具有实现一般智能行为的充分必要手段。",
 src="Computer Science as Empirical Inquiry: Symbols and Search, Communications of the ACM 19(3), p.116（经维基百科引用核对）",url="https://doi.org/10.1145/360018.360022",type="paper",status="二手核对（原刊付费，引文经百科转引）",archive="newell_wiki.txt")
e(id="rosenblatt-1958",cat="school",stance="na",person="Frank Rosenblatt",role="连接主义先驱；代表系统 感知机",date="1958",
 quote="The perceptron: a probabilistic model for information storage and organization in the brain.",
 zh="《感知机：大脑中信息存储与组织的概率模型》（论文标题）",
 src="Psychological Review 65(6):386–408",url="https://doi.org/10.1037/h0042519",type="paper",status="原文核实（标题，经 Europe PMC）",archive="")
e(id="sep-connectionism",cat="school",stance="na",person="Stanford Encyclopedia of Philosophy",role="连接主义词条",date="2019",
 quote="Connectionism is a movement in cognitive science that hopes to explain intellectual abilities using artificial neural networks (also known as “neural networks” or “neural nets”).",
 zh="连接主义是认知科学中的一场运动，希望用人工神经网络来解释智能能力。",
 src="SEP: Connectionism",url="https://plato.stanford.edu/entries/connectionism/",type="encyclopedia",status="原文核实",archive="sep_conn.txt")
e(id="sutton-2019",cat="school",stance="na",person="Rich Sutton",role="强化学习奠基人，2024 图灵奖",date="2019-03-13",
 quote="The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin.",
 zh="从 70 年 AI 研究中能读出的最大教训是：利用算力的通用方法最终最有效，而且优势巨大。",
 src="The Bitter Lesson",url="http://www.incompleteideas.net/IncIdeas/BitterLesson.html",type="official",status="原文核实",archive="bitter.txt")
e(id="brooks-1991",cat="school",stance="na",person="Rodney Brooks",role="行为主义/具身机器人；代表系统 包容式架构机器人",date="1991",
 quote="When we examine very simple level intelligence we find that explicit representations and models of the world simply get in the way. It turns out to be better to use the world as its own model.",
 zh="考察很简单层级的智能时我们发现，显式的表征和世界模型只会碍事。事实证明，让世界充当它自己的模型更好。",
 src="Intelligence without representation, Artificial Intelligence 47:139–159",url="https://people.csail.mit.edu/brooks/papers/representation.pdf",type="paper",status="原文核实",archive="brooks.txt")
e(id="paper-deepblue",cat="school",stance="na",person="祁玉（讲座）",role="符号主义案例",date="2026-10-21",
 quote="“深蓝”系统依据棋局规则，以每秒评估约两亿个局面的速度搜索可能的走法，从中选择落子方案。",zh="",
 src="澎湃新闻讲座整理稿",url="https://m.thepaper.cn/newsDetail_forward_34390827",type="news",status="原文核实（整理稿）",archive="paper.txt")
e(id="paper-sym-limit",cat="school",stance="open",person="祁玉（讲座）",role="符号主义能否通向意识",date="2026-10-21",
 quote="如果意识能够被描述清楚，并转化为机器可处理的符号与规则，那么就能进一步探索其在机器中实现的可能。但问题在于，人能将意识本身描述得透彻吗？",zh="",
 src="澎湃新闻讲座整理稿",url="https://m.thepaper.cn/newsDetail_forward_34390827",type="news",status="原文核实（整理稿）",archive="paper.txt")
e(id="paper-rl",cat="school",stance="na",person="祁玉（讲座）",role="行为主义路径",date="2026-10-21",
 quote="“强化学习”（Reinforcement Learning，RL）是实现这一思路的重要方法：让机器在不断尝试中，根据环境反馈调整行动。",zh="",
 src="澎湃新闻讲座整理稿",url="https://m.thepaper.cn/newsDetail_forward_34390827",type="news",status="原文核实（整理稿）",archive="paper.txt")
S={"paper-three-paths":["sym","con","beh"],"paper-deepblue":["sym"],"paper-sym-limit":["sym"],"paper-rl":["beh"],"dartmouth-1955":["sym","con"],"newell-simon-1976":["sym"],"searle":["sym"],"hot":["sym"],"gwt":["sym","con"],
"rosenblatt-1958":["con"],"sep-connectionism":["con"],"hinton-2006":["con"],"nobel-2024":["con"],"dehaene-2017":["con"],"ast":["con"],"butlin-2023":["con"],"chalmers-2023":["con"],"anth-introspection":["con"],"opus4-bliss":["con","beh"],"sutskever-2022":["con"],"hinton-stewart":["con"],"hinton-bigtech":["con"],"welfare-2024":["con"],"paper-brain-align":["con"],"sutton-2019":["con","beh"],
"turing-1950":["beh"],"brooks-1991":["beh"],"seth-bbs":["beh"],"seth-ted":["beh"],"nyd-animal":["beh"],"folk-2024":["beh"],"lemoine-2022":["beh"],"google-lemoine":["beh"],"google-lemoine-bbc":["beh"],"suleyman-2025":["beh"],"vatican-2026":["beh"]}
for x in E: x["schools"]=S.get(x["id"],[])
json.dump({"topic":"AI 有意识吗？","updated":A,"items":E},open("data/evidence.json","w"),ensure_ascii=False,indent=1)
print("with schools",len(E))

# ======== 第二轮：滚雪球扩展（2026-11-04）========
def n(**k):
    k.setdefault("accessed",A); k.setdefault("schools",[]); E.append(k)
EPMC="https://europepmc.org/article/MED/"
n(id="koch-2016-ncc",cat="science",stance="na",person="Koch, Massimini, Boly, Tononi",role="神经相关物（NCC）综述",date="2016",
 quote="the anatomical neural correlates of consciousness are primarily localized to a posterior cortical hot zone that includes sensory areas, rather than to a fronto-parietal network involved in task monitoring and reporting.",
 zh="意识的解剖学神经相关物主要位于包含感觉区的“后部皮层热区”，而不是负责任务监控与报告的额顶网络。",
 src="Nature Reviews Neuroscience 17:307–321",url="https://doi.org/10.1038/nrn.2016.22",type="paper",status="原文核实（摘要）",archive="koch2016.txt",cites=["iit4"])
n(id="cogitate-2025",cat="science",stance="na",person="Cogitate Consortium",role="对抗性合作（IIT vs GNWT），n=256",date="2025",
 quote="These results align with some predictions of IIT and GNWT, while substantially challenging key tenets of both theories.",
 zh="结果与 IIT 和 GNWT 的部分预测一致，同时对两者的关键主张构成实质挑战。",
 src="Nature 642（2025）",url="https://doi.org/10.1038/s41586-025-08888-1",type="paper",status="原文核实（摘要）",archive="cogitate2025.txt",cites=["iit4","gwt","cogitate","mashour-2020"])
n(id="mashour-2020",cat="science",stance="na",person="Mashour, Roelfsema, Changeux, Dehaene",role="全局神经工作空间综述",date="2020",
 quote="The GNW hypothesis proposes that, in the conscious state, a non-linear network ignition associated with recurrent processing amplifies and sustains a neural representation, allowing the corresponding information to be globally accessed by local processors.",
 zh="GNW 假说认为：意识状态下，伴随循环加工的非线性网络“点燃”放大并维持某个神经表征，使相应信息可被各局部处理器全局访问。",
 src="Neuron 105(5):776–798",url="https://doi.org/10.1016/j.neuron.2020.01.026",type="paper",status="原文核实（摘要）",archive="mashour2020.txt",cites=["gwt","dehaene-2017"])
n(id="tononi-2016",cat="science",stance="na",person="Tononi, Boly, Massimini, Koch",role="IIT 综述",date="2016",
 quote="It argues that the physical substrate of consciousness must be a maximum of intrinsic cause-effect power and provides a means to determine, in principle, the quality and quantity of experience.",
 zh="IIT 认为意识的物理基底必须是内在因果力的极大值，并在原则上给出确定体验质与量的方法。",
 src="Nature Reviews Neuroscience 17:450–461",url="https://doi.org/10.1038/nrn.2016.44",type="paper",status="原文核实（摘要）",archive="tononi2016.txt",cites=["iit4"])
n(id="alkire-2008",cat="science",stance="na",person="Alkire, Hudetz, Tononi",role="麻醉与意识",date="2008",
 quote="Thus, anesthetics seem to cause unconsciousness when they block the brain's ability to integrate information.",
 zh="因此，麻醉剂似乎是在阻断大脑整合信息的能力时导致无意识的。",
 src="Science 322:876–880",url="https://doi.org/10.1126/science.1149213",type="paper",status="原文核实（摘要）",archive="alkire2008.txt",cites=["tononi-2016"])
n(id="casali-2013",cat="science",stance="na",person="Casali, Massimini 等",role="扰动复杂度指数 PCI",date="2013",
 quote="PCI reliably discriminated the level of consciousness in single individuals during wakefulness, sleep, and anesthesia, as well as in patients who had emerged from coma and recovered a minimal level of consciousness.",
 zh="PCI 能在个体层面可靠区分清醒、睡眠、麻醉下的意识水平，也能区分从昏迷中苏醒并恢复最低意识的患者。",
 src="Science Translational Medicine 5(198):198ra105",url="https://doi.org/10.1126/scitranslmed.3006294",type="paper",status="原文核实（摘要）",archive="casali2013.txt",cites=["alkire-2008","tononi-2016"])
n(id="owen-2006",cat="science",stance="na",person="Owen, Coleman, Boly, Davis, Laureys, Pickard",role="植物状态中的隐性意识",date="2006",
 quote="When asked to imagine playing tennis or moving around her home, the patient activated predicted cortical areas in a manner indistinguishable from that of healthy volunteers.",
 zh="当被要求想象打网球或在家中走动时，这位被诊断为植物状态的患者激活了预期的皮层区域，与健康志愿者无法区分。",
 src="Science 313:1402",url="https://doi.org/10.1126/science.1130197",type="paper",status="原文核实（摘要）",archive="owen2006.txt",cites=[],schools=["beh"],note="行为缺席≠意识缺席：对“以行为判意识”的直接反例。")
n(id="monti-2010",cat="science",stance="na",person="Monti, Laureys, Owen 等",role="意识障碍中的意愿性脑活动（54 例）",date="2010",
 quote="These results show that a small proportion of patients in a vegetative or minimally conscious state have brain activation reflecting some awareness and cognition.",
 zh="结果表明，少部分植物状态或最低意识状态患者有反映一定觉知与认知的脑激活。",
 src="NEJM 362:579–589",url="https://doi.org/10.1056/NEJMoa0905370",type="paper",status="原文核实（摘要）",archive="monti2010.txt",cites=["owen-2006"],schools=["beh"])
n(id="gazzaniga-2005",cat="science",stance="na",person="Michael Gazzaniga",role="裂脑研究",date="2005",
 quote="Split-brain methodology, on its own and in conjunction with neuroimaging, has yielded insights into the remarkable regional specificity of the corpus callosum as well as into the integrative role of the callosum in the perception of causality and in our perception of an integrated sense of self.",
 zh="裂脑方法揭示了胼胝体的区域特异性，以及它在因果知觉和“统一自我感”中的整合作用。",
 src="Nature Reviews Neuroscience 6:653–659",url="https://doi.org/10.1038/nrn1723",type="paper",status="原文核实（摘要）",archive="gazzaniga2005.txt",cites=[])
n(id="blindsight-2010",cat="science",stance="na",person="Sahraie, Weiskrantz 等",role="盲视（患者 D.B.）",date="2010",
 quote="This phenomenon, termed \"blindsight,\" is intriguing because it demonstrates a dissociation between detection and perception.",
 zh="这种被称为“盲视”的现象之所以引人注目，是因为它显示了“探测”与“知觉”可以分离。",
 src="PNAS 107(49):21217–21222",url="https://doi.org/10.1073/pnas.1015652107",type="paper",status="原文核实（摘要）",archive="weisk2010.txt",cites=[],schools=["beh"],note="能正确反应却报告“没看见”：功能与体验可以分离——这正是判断 AI 时的核心难点。")
n(id="seth-bayne-2022",cat="theory",stance="na",person="Anil Seth & Tim Bayne",role="意识理论综述",date="2022",
 quote="we review four prominent theoretical approaches to consciousness: higher-order theories, global workspace theories, re-entry and predictive processing theories and integrated information theory.",
 zh="我们综述四大意识理论路径：高阶理论、全局工作空间理论、再入与预测加工理论、整合信息理论。",
 src="Nature Reviews Neuroscience 23:439–452",url="https://doi.org/10.1038/s41583-022-00587-4",type="paper",status="原文核实（摘要）",archive="seth2022.txt",cites=["hot","gwt","iit4","seth-bbs"])
n(id="levine-gap",cat="philosophy",stance="na",person="Stanford Encyclopedia of Philosophy（转述 Levine 1983）",role="解释鸿沟",date="1983 / SEP",
 quote="Our current inability to supply a suitably intelligible link is sometimes described, following Joseph Levine (1983), as the existence of an explanatory gap",
 zh="我们目前无法提供一个足够可理解的联结——继 Levine（1983）之后，这常被称为“解释鸿沟”。",
 src="SEP: Consciousness §5.2",url="https://plato.stanford.edu/entries/consciousness/",type="encyclopedia",status="转述（经 SEP）",archive="sep_con.txt",cites=["chalmers-1995","nagel-1974"])
n(id="mary-jackson",cat="philosophy",stance="na",person="Frank Jackson（经 SEP 引）",role="知识论证 / 玛丽的房间",date="1982",
 quote="Mary is a brilliant scientist who is, for whatever reason, forced to investigate the world from a black and white room via a black and white television monitor.",
 zh="玛丽是一位出色的科学家，出于某种原因只能在黑白房间里通过黑白电视研究世界。（她掌握关于颜色的全部物理知识——走出房间看到红色时，她学到了新东西吗？）",
 src="SEP: Qualia: The Knowledge Argument",url="https://plato.stanford.edu/entries/qualia-knowledge/",type="encyclopedia",status="原文核实（SEP 引 Jackson 1982）",archive="sep_qualia-knowledge.txt",cites=[],note="括号内追问为编者概括。")
n(id="panpsychism",cat="philosophy",stance="open",person="Stanford Encyclopedia of Philosophy",role="泛心论",date="2022",
 quote="Panpsychism is the view that mentality is fundamental and ubiquitous in the natural world.",
 zh="泛心论认为，心性在自然界中是基本的、无处不在的。",
 src="SEP: Panpsychism",url="https://plato.stanford.edu/entries/panpsychism/",type="encyclopedia",status="原文核实",archive="sep_panpsychism.txt",cites=["chalmers-1995"])
n(id="frankish-2016",cat="philosophy",stance="na",person="Keith Frankish",role="错觉论",date="2016",
 quote="This is the view that phenomenal consciousness, as usually conceived, is illusory. ... the hard problem is replaced by the illusion problem.",
 zh="错觉论认为，通常理解的现象意识是一种错觉……“难问题”被“错觉问题”取代。",
 src="Journal of Consciousness Studies 23(11–12):11–39（作者接受稿）",url="https://keithfrankish.github.io/articles/Frankish_2016_Illusionism_as_a_theory_of_consciousness_eprint.pdf",type="paper",status="原文核实",archive="frankish2016.txt",cites=["chalmers-1995"],note="若错觉论为真，AI 是否“有意识”就变成它是否也有同样的自我表征错觉——这让问题更可检验。（编者）")
n(id="hot-sep",cat="philosophy",stance="na",person="Stanford Encyclopedia of Philosophy",role="高阶理论词条",date="2026",
 quote="Higher-order theories of consciousness try to explain the difference between unconscious and conscious mental states in terms of a relation obtaining between the conscious state in question and a higher-order representation of some sort",
 zh="高阶理论试图用“该状态与某种高阶表征之间的关系”来解释有意识与无意识心理状态的差别。",
 src="SEP: Higher-Order Theories of Consciousness",url="https://plato.stanford.edu/entries/consciousness-higher/",type="encyclopedia",status="原文核实",archive="sep_consciousness-higher.txt",cites=["hot"],schools=["sym"])
n(id="cambridge-2012",cat="animal",stance="na",person="Philip Low 执笔；Panksepp、Reiss、Edelman、Van Swinderen、Koch 编",role="剑桥意识宣言",date="2012-07-07",
 quote="Consequently, the weight of evidence indicates that humans are not unique in possessing the neurological substrates that generate consciousness. Non-human animals, including all mammals and birds, and many other creatures, including octopuses, also possess these neurological substrates.",
 zh="因此，证据的分量表明，人类并非唯一拥有产生意识之神经基底的物种。包括所有哺乳动物和鸟类在内的非人动物，以及章鱼等许多其他生物，也拥有这些神经基底。",
 src="The Cambridge Declaration on Consciousness",url="https://www.ocf.berkeley.edu/~jfkihlstrom/ConsciousnessWeb/PDFs/CambridgeDeclarationOnConsciousness.pdf",type="official",status="原文核实",archive="cambridge2012.txt",cites=[],schools=["beh"])
n(id="butlin-2026",cat="ai",stance="open",person="Butlin, Long, Bayne, Bengio, Birch, Chalmers 等",role="AI 意识指标方法（TiCS）",date="2026",
 quote="Indicators derived from such theories can be used to inform credences about whether particular AI systems are conscious.",
 zh="从这些理论推导出的指标，可用来为“某个 AI 系统是否有意识”的可信度提供依据。",
 src="Trends in Cognitive Sciences（2026）",url="https://doi.org/10.1016/j.tics.2025.10.011",type="paper",status="原文核实（摘要）",archive="butlin2026.txt",cites=["butlin-2023","gwt","hot","iit4"],schools=["con"])
n(id="openai-jang-2025",cat="ai",stance="open",person="Joanne Jang（OpenAI 模型行为负责人）",role="OpenAI 立场",date="2025-06",
 quote="Ontological consciousness isn’t something we consider scientifically resolvable without clear, falsifiable tests, whereas perceived consciousness can be explored through social science research.",
 zh="在没有清晰、可证伪的测试之前，我们不认为“本体意识”在科学上可以解决；而“被感知的意识”可以通过社会科学研究来探索。",
 src="Some thoughts on human-AI relationships（作者 Substack，OpenAI 同步发布）",url="https://reservoirsamples.substack.com/p/some-thoughts-on-human-ai-relationships",type="official",status="原文核实",archive="jang2025.txt",cites=[],schools=["beh"])
n(id="zeng-yi-2025",cat="china",stance="no",person="曾毅（中科院自动化所研究员，联合国 AI 高层顾问机构专家）",role="中国学者",date="2025-02-28",
 quote="现在的人工智能技术，它能够分析人类的情感，能够对人类的情感做出一些回应。但是它不是真正具有情感。它没有生命，也没有真正的意识，现在确实也不是真正意义的人类的伙伴，只是一个工具。",zh="",
 src="中国网专访（新浪转载）",url="https://news.sina.com.cn/zx/gj/2025-02-28/doc-inemyxcv0195880.shtml",type="news",status="原文核实（访谈整理）",archive="zeng_china.txt",cites=[],schools=["beh","con"],note="他同时认为生成式 AI“在行为上模仿人类智能，还不是从机制上模仿”。")
n(id="zhu-songchun",cat="china",stance="no",person="朱松纯（北京通用人工智能研究院院长）",role="中国学者",date="2024/2025",
 quote="该论文指出大模型无异于“缸中之脑”，因为大模型本身并不存在于真实世界中，无法像人一样实现从“词语（word）”到“世界（world）”的联结。",zh="",
 src="《为机器立心》第一章摘录（知识分子·财新博客）",url="https://zhishifenzi.blog.caixin.com/archives/280608",type="book",status="原文核实（书摘）",archive="zhu_caixin.txt",cites=["searle"],schools=["sym","beh"],note="符号落地问题与 Searle 中文屋同源；他主张“价值驱动”的认知架构，统一符号逻辑与统计学习。")

n(id="block-1995",cat="define",stance="na",person="Ned Block",role="现象意识 vs 取用意识",date="1995",
 quote="Consciousness is a mongrel concept: there are a number of very different \"consciousnesses.\" Phenomenal consciousness is experience; the phenomenally conscious aspect of a state is what it is like to be in that state. The mark of access-consciousness, by contrast, is availability for use in reasoning and rationally guiding speech and action.",
 zh="“意识”是个混杂概念：存在多种很不相同的“意识”。现象意识就是体验——一个状态的现象意识层面，就是处于该状态“是什么感觉”。取用意识的标志则是：可被用于推理，并理性地引导言语与行动。",
 src="Behavioral and Brain Sciences 18(2):227–247（Cogprints 预印本）",url="https://web-archive.southampton.ac.uk/cogprints.org/231/1/199712004.html",type="paper",status="原文核实（摘要）",archive="block1995.txt",cites=["nagel-1974"],schools=["con","beh"],note="本专题问的是现象意识。取用意识是功能概念，大模型在相当程度上已具备类似功能——这恰恰不能回答现象意识问题。")
n(id="sep-varieties",cat="define",stance="na",person="Stanford Encyclopedia of Philosophy",role="意识的多种含义",date="2026",
 quote="One can refer specifically to phenomenal consciousness, access consciousness, reflexive or meta-mental consciousness, and narrative consciousness among other varieties.",
 zh="人们可以具体指称现象意识、取用意识、反身或元心理意识（自我意识）、叙事意识等多种意识。",
 src="SEP: Consciousness §2",url="https://plato.stanford.edu/entries/consciousness/",type="encyclopedia",status="原文核实",archive="sep_con.txt",cites=["block-1995"])
n(id="sep-sentience",cat="define",stance="na",person="Stanford Encyclopedia of Philosophy",role="感受性与自我意识",date="2026",
 quote="It may be conscious in the generic sense of simply being a sentient creature, one capable of sensing and responding to its world (Armstrong 1981). ... A third and yet more demanding sense might define conscious creatures as those that are not only aware but also aware that they are aware, thus treating creature consciousness as a form of self-consciousness (Carruthers 2000).",
 zh="在一般意义上，一个生物“有意识”可以只是指它有感受性（sentience）——能感知并回应世界；更苛刻的意义则要求它不仅觉知，还觉知到自己在觉知，即自我意识。",
 src="SEP: Consciousness §2.1",url="https://plato.stanford.edu/entries/consciousness/",type="encyclopedia",status="原文核实",archive="sep_con.txt",cites=[],note="注意：动物福利与 AI 福利文献中的 sentience 常特指“有正负效价的体验”（能受苦/感到好），比 SEP 此处的一般义更窄。")
# 重新归类：澎湃文章降为普通来源
R={"paper-lecture":"school","paper-three-paths":"school","hinton-2006":"school","nobel-2024":"school","turing-1950":"test","butlin-2026":"test","openai-jang-2025":"stance","cogitate":"theory","iit-pseudo":"theory","cogitate-2025":"theory","nyd-animal":"animal",
   "paper-brain-align":"ai","chalmers-2023":"ai","anth-introspection":"ai","opus4-bliss":"ai","folk-2024":"ai","lemoine-2022":"ai","paper-buddhism":"philosophy","nagel-1974":"define","chalmers-1995":"philosophy","iep-hard":"philosophy","searle":"philosophy"}
C={"butlin-2023":["gwt","iit4","hot","ast","seth-bbs","nyd-animal"],"chalmers-2023":["butlin-2023","lemoine-2022","gwt","iit4"],"cogitate":["iit4","gwt"],"iit-pseudo":["iit4","cogitate"],"anth-welfare":["welfare-2024","chalmers-2023"],"welfare-2024":["butlin-2023","nyd-animal"],"anth-end":["anth-welfare"],"google-lemoine":["lemoine-2022"],"google-lemoine-bbc":["lemoine-2022"],"iep-hard":["chalmers-1995"],"chalmers-1995":["nagel-1974"],"nyd-animal":["cambridge-2012"],"suleyman-2025":["butlin-2023"],"paper-three-paths":["dartmouth-1955","rosenblatt-1958","brooks-1991"],"sutton-2019":["paper-deepblue"],"hinton-bigtech":["hinton-2006"],"opus4-bliss":["anth-welfare"],"anth-introspection":["hot"],"seth-ted":["seth-bbs"],"dehaene-2017":["gwt"]}
for x in E:
    x["cat"]=R.get(x["id"],x["cat"]); x.setdefault("cites",[])
    x["cites"]=sorted(set(x["cites"])|set(C.get(x["id"],[])))
    if x["cat"]=="origin": x["cat"]="school"
ids={x["id"] for x in E}
for x in E:
    bad=[c for c in x["cites"] if c not in ids]; assert not bad,(x["id"],bad)
exec(open("data/media.py",encoding="utf-8").read())
json.dump({"topic":"AI 有意识吗？","updated":A,"items":E,"media":M},open("data/evidence.json","w"),ensure_ascii=False,indent=1)
print("round2",len(E),"items",len(M),"media")
