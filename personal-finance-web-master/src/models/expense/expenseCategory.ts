export interface IExpenseSubCategory {
  id: number
  name: string
  icon: any
}

export interface IExpenseCategory {
  id: number
  name: string
  icon: any
  sub_category: IExpenseSubCategory[]
}
