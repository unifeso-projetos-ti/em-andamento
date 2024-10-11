'use client'

import Image from 'next/image'
import { ReactNode, useState } from 'react'
import {
  Logo,
  LogoIcon,
  Sidebar,
  SidebarBody,
  SidebarLink,
  SidebarProvider,
} from '..'
import { IRoutes } from '../..'

interface SidebarLayoutProps {
  children: ReactNode
  routes: IRoutes[]
}

export const SidebarLayout = ({ children, routes }: SidebarLayoutProps) => {
  const [open, setOpen] = useState(false)

  return (
    <SidebarProvider>
      <div className="flex-col md:flex-row flex h-screen overflow-hidden w-full">
        <Sidebar open={open} setOpen={setOpen}>
          <SidebarBody className="justify-between gap-10">
            <div className="flex flex-col flex-1 overflow-y-auto overflow-x-hidden">
              {open ? <Logo /> : <LogoIcon />}
              <div className="mt-8 flex flex-col gap-2">
                {routes.map((route, idx) => (
                  <SidebarLink key={idx} link={route} />
                ))}
              </div>
            </div>
            <div>
              <SidebarLink
                link={{
                  name: 'Kauan Vieira Xavier',
                  router: '#',
                  icon: (
                    <Image
                      src={'icons/noclaf-logo.svg'}
                      className="h-7 w-7 flex-shrink-0 rounded-full"
                      width={50}
                      height={50}
                      alt="Avatar"
                    />
                  ),
                }}
              />
            </div>
          </SidebarBody>
        </Sidebar>
        <main className="flex-1 h-full p-4 md:p-10 rounded-tl-2xl border border-light-border-color-navigation dark:border-dark-border-color-navigation bg-light-background dark:bg-dark-background-activate-route overflow-y-auto">
          <div className="flex flex-col h-full gap-4 ">{children}</div>
        </main>
      </div>
    </SidebarProvider>
  )
}
