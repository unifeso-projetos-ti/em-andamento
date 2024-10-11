import { IExpenseCategory } from 'src/models/expense/expenseCategory'

export const EXPENSE_CATEGORIES: IExpenseCategory[] = [
  {
    id: 1,
    name: 'Saúde',
    icon: `kauanvieiraxavierdev@gmail.com`,
    sub_category: [
      {
        id: 1,
        name: 'Farmácia',
        icon: `kauanvieiraxavierdev@gmail.com`,
      },
    ],
  },
  {
    id: 2,
    name: 'Educação',
    icon: `kauanvieiraxavierdev@gmail.com`,
    sub_category: [
      {
        id: 1,
        name: 'Faculdade',
        icon: `kauanvieiraxavierdev@gmail.com`,
      },
    ],
  },
  {
    id: 3,
    name: 'Lazer',
    icon: `biacapacia@gmail.com`,
    sub_category: [
      {
        id: 1,
        name: 'Cinema',
        icon: `kauanvieiraxavierdev@gmail.com`,
      },
    ],
  },
]
