export interface IExpense {
  category: number
  sub_category: number
  costs: number
  date: string
  user: number
}

export interface IDataExpense {
  id: string
  expense: IExpense
}
