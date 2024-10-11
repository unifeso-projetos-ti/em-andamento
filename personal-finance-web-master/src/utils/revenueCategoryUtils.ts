import { REVENUE_CATEGORIES } from 'public/constants/revenue/revenueCategory'
import { IRevenueCategory } from 'src/models/category'

export const getRevenueCategoryById = (
  categoryId: number
): IRevenueCategory | undefined => {
  return REVENUE_CATEGORIES.find((category) => category.id === categoryId)
}
