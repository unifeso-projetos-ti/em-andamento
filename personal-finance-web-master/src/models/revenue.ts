export interface IRevenue {
  category: number
  costs: number
  date: string
  user: number
}

export interface IDataRevenue {
  id: string
  revenue: IRevenue
}
