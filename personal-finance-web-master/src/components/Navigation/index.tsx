'use client'

import { ReactNode } from 'react'
import NavbarComponent from './navbar'
import { SidebarLayout } from './sidebar/layout-sidebar'

export interface IRoutes {
  name: string
  router: string
  icon?: any
}

interface SidebarProps {
  children: ReactNode
  type: 'Navbar' | 'Sidebar'
  routes: IRoutes[]
}

export interface NavigationProps {
  router: IRoutes[]
}

export const Navigation = ({ children, type, routes }: SidebarProps) => {
  return (
    <div className="flex size-full dark:bg-dark-background-navigation-bar bg-light-background-navigation-bar">
      {type === 'Sidebar' && (
        <SidebarLayout routes={routes}>{children}</SidebarLayout>
      )}
      <div className="size-full flex-1 flex-col ">
        {type === 'Navbar' && (
          <>
            <NavbarComponent router={routes} />
            <main className="mt-4 h-full w-full overflow-visible">
              <div className="flex h-[90%] w-full flex-col gap-4">
                {children}
              </div>
            </main>
          </>
        )}
      </div>
    </div>
  )
}
