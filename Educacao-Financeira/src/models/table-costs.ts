export interface ICategoryCosts {
  name: string
  icon: string
}

export interface ISubCategoryCosts {
  name: string
  icon: string
}

export interface ITableCostsData {
  id: number
  name: string
  email: string
  avatar: string
  is_recurrent: boolean
  recurrently: number
  category: ICategoryCosts
  sub_category: ISubCategoryCosts
  financial_transactions: number
}

export interface ITableExpensesData {
  id: number
  name: string
  email: string
  avatar: string
  is_recurrent: boolean
  category: ICategoryCosts
  financial_transactions: number
}
