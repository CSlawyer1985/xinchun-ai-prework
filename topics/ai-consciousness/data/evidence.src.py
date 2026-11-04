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
