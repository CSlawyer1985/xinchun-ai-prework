export type AlumniMember = {
  name: string
  note?: string
  image: string
}

export type AlumniCohort = {
  title: string
  season: string
  members: AlumniMember[]
}

export const alumniCohorts: AlumniCohort[] = [
  {
    title: '第一期学员',
    season: '同行者',
    members: [
      { name: 'Eliza', image: '/images/students/Eliza.jpg' },
      { name: 'IBU', image: '/images/students/IBU.jpg' },
      { name: 'Will', image: '/images/students/Will.jpg' },
      { name: 'WrongLei', note: '律师', image: '/images/students/WrongLei 律师.jpg' },
      { name: 'Zhan', image: '/images/students/Zhan.jpg' },
      { name: 'Weiweierbee', image: '/images/students/weiweierbee.jpg' },
      { name: '刘一洲', image: '/images/students/刘一洲.jpg' },
      { name: '刘林杰', image: '/images/students/刘林杰.jpg' },
      { name: '卜未鸣', image: '/images/students/卜未鸣.jpg' },
      { name: '卢思琦', image: '/images/students/卢思琦.jpg' },
      { name: '周芃芃', note: '律师', image: '/images/students/周芃芃律师.jpg' },
      { name: '宫致成', note: 'Robert', image: '/images/students/宫致成_Robert.jpg' },
      { name: '指针', image: '/images/students/指针.jpg' },
      { name: '李子豪', note: '君泽君', image: '/images/students/李子豪律师  「君泽君」.jpg' },
      { name: '林晓琳', image: '/images/students/林晓琳.jpg' },
      { name: '毛线球', image: '/images/students/毛线球。.jpg' },
      { name: '董远航', image: '/images/students/董远航.jpg' },
      { name: '郑玲珠', image: '/images/students/郑玲珠.jpg' }
    ]
  },
  {
    title: '第二期学员',
    season: '同行者',
    members: [
      { name: 'Wensley', image: '/images/students/Wensley.jpg' },
      { name: '陈可妮', image: '/images/students/陈可妮.jpg' },
      { name: '陈旸', image: '/images/students/陈旸.jpg' },
      { name: '丁铭', image: '/images/students/丁铭.jpg' },
      { name: '郭治年', image: '/images/students/郭治年.jpg' },
      { name: '郝韶泽', image: '/images/students/郝韶泽.jpg' },
      { name: '黄婉晴', image: '/images/students/黄婉晴.jpg' },
      { name: '老炊', image: '/images/students/老炊.jpg' },
      { name: '李震东', image: '/images/students/李震东.jpg' },
      { name: '林骥', image: '/images/students/林骥.jpg' },
      { name: '凌鹏飞', image: '/images/students/凌鹏飞.jpg' },
      { name: '刘佳馨', image: '/images/students/刘佳馨.jpg' },
      { name: '马骥一', image: '/images/students/马骥一.jpg' },
      { name: '毛依玲', image: '/images/students/毛依玲.jpg' },
      { name: '牛晓鑫', image: '/images/students/牛晓鑫.jpg' },
      { name: '钱驾浩', image: '/images/students/钱驾浩.jpg' },
      { name: '沈燕', image: '/images/students/沈燕.jpg' },
      { name: '苏成鹏', image: '/images/students/苏成鹏.jpg' },
      { name: '汪蓉', image: '/images/students/汪蓉.jpg' },
      { name: '王嘉璐', image: '/images/students/王嘉璐.jpg' },
      { name: '王静蕾', image: '/images/students/王静蕾.jpg' },
      { name: '王仲志', image: '/images/students/王仲志.jpg' },
      { name: '魏宏岩', image: '/images/students/魏宏岩.jpg' },
      { name: '邬晓霞', image: '/images/students/邬晓霞.jpg' },
      { name: '吴夙现', image: '/images/students/吴夙现.jpg' },
      { name: '徐海燕', image: '/images/students/徐海燕.jpg' },
      { name: '徐翔', image: '/images/students/徐翔.jpg' },
      { name: '徐幸杰', image: '/images/students/徐幸杰.jpg' },
      { name: '徐扬', image: '/images/students/徐扬.jpg' },
      { name: '许珩', image: '/images/students/许珩.jpg' },
      { name: '袁红姣', image: '/images/students/袁红姣.jpg' },
      { name: '章大成', image: '/images/students/章大成.jpg' },
      { name: '赵晖', image: '/images/students/赵晖.jpg' },
      { name: '郑姗儿', image: '/images/students/郑姗儿.jpg' },
      { name: '朱媛', image: '/images/students/朱媛.jpg' }
    ]
  }
]
