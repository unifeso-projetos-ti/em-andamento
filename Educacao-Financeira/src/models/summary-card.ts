import { ReactNode } from 'react'

export interface ISummaryCard {
  title: string
  component?: ReactNode
  total: number
  percentage: number
  text_percentage: string
}
