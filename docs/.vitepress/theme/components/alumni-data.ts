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
      { name: '李震东', note: '律师', image: '/images/students/李震东律师.jpg' },
      { name: '林晓琳', image: '/images/students/林晓琳.jpg' },
      { name: '毛线球', image: '/images/students/毛线球。.jpg' },
      { name: '董远航', image: '/images/students/董远航.jpg' },
      { name: '郑玲珠', image: '/images/students/郑玲珠.jpg' }
    ]
  }
]
