import { EXPENSE_CATEGORIES } from 'public/constants/expense/expenseCategory'
import {
  IExpenseCategory,
  IExpenseSubCategory,
} from 'src/models/expense/expenseCategory'

export const getExpenseCategoryById = (
  categoryId: number
): IExpenseCategory | undefined => {
  return EXPENSE_CATEGORIES.find((category) => category.id === categoryId)
}

export const getExpenseSubCategoryById = (
  categoryId: number,
  subCategoryId: number
): IExpenseSubCategory | undefined => {
  const category = EXPENSE_CATEGORIES.find(
    (category) => category.id === categoryId
  )

  if (category) {
    return category.sub_category.find((sub) => sub.id === subCategoryId)
  }

  return undefined
}
