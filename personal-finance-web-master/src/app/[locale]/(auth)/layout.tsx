import {
  IconAddressBook,
  IconHome,
  IconLayout,
  IconReportMoney,
} from '@tabler/icons-react'
import { ReactNode } from 'react'
import { IRoutes, Navigation } from '../../../components/Navigation'

interface LayoutProps {
  children: ReactNode
}
export default function AuthLayout({ children }: LayoutProps) {
  const router: IRoutes[] = [
    {
      name: 'home',
      router: '/',
      icon: (
        <IconHome className="dark:text-dark-icon-color text-light-icon-color size-5 flex-shrink-0" />
      ),
    },
    {
      name: 'dashboard',
      router: '/dashboard',
      icon: (
        <IconLayout className="dark:text-dark-icon-color text-light-icon-color size-5 flex-shrink-0" />
      ),
    },
    {
      name: 'receita',
      router: '/revenue',
      icon: (
        <IconReportMoney className="dark:text-dark-icon-color text-light-icon-color size-5 flex-shrink-0" />
      ),
    },
    {
      name: 'despesas',
      router: '/expenses',
      icon: (
        <IconAddressBook className="dark:text-dark-icon-color text-light-icon-color size-5 flex-shrink-0" />
      ),
    },
  ]

  return (
    <Navigation routes={router} type="Sidebar">
      {children}
    </Navigation>
  )
}
