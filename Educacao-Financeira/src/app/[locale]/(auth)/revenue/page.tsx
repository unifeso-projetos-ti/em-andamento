'use client'

import {
  Button,
  Dropdown,
  DropdownItem,
  DropdownMenu,
  DropdownTrigger,
  Pagination,
  Selection,
  SortDescriptor,
  Table,
  TableBody,
  TableCell,
  TableColumn,
  TableHeader,
  TableRow,
  Tooltip,
  useDisclosure,
  User,
} from '@nextui-org/react'
import { IconChevronDown, IconPlus, IconTrash } from '@tabler/icons-react'
import { columnsCosts } from 'public/constants/revenue-table/data'
import React, { useEffect, useState } from 'react'
import { deleteRevenue, getRevenues } from 'service/revenue/revenue'
import ConfirmModal from 'src/components/modals'
import CreateCostModal from 'src/components/modals/revenue'
import { IRevenueCategory } from 'src/models/category'
import { IDataRevenue } from 'src/models/revenue'
import { IUser } from 'src/models/user'
import { capitalize } from 'src/utils/capitalize'
import { formatCurrency } from 'src/utils/currency'
import { getRevenueCategoryById } from 'src/utils/revenueCategoryUtils'
import { useFormattedDate } from 'src/utils/useFormatDate'
import { getUserById } from 'src/utils/userUtils'

const INITIAL_VISIBLE_COLUMNS = ['user', 'category', 'costs', 'date', 'actions']

export default function Costs() {
  const { formatDateString } = useFormattedDate()
  const [selectedRevenueId, setSelectedRevenueId] = useState<string>('0')
  const [filterValue, setFilterValue] = React.useState('')
  const [selectedKeys, setSelectedKeys] = React.useState<Selection>(new Set([]))
  const [visibleColumns, setVisibleColumns] = React.useState<Selection>(
    new Set(INITIAL_VISIBLE_COLUMNS)
  )
  const [statusFilter, setStatusFilter] = React.useState<Selection>('all')
  const [rowsPerPage, setRowsPerPage] = React.useState(5)
  const [sortDescriptor, setSortDescriptor] = React.useState<SortDescriptor>({
    column: 'name',
    direction: 'ascending',
  })
  const { isOpen, onOpen, onClose } = useDisclosure()
  const {
    isOpen: isOpenDelete,
    onOpen: onOpenDelete,
    onClose: onCloseDelete,
  } = useDisclosure()
  const [page, setPage] = React.useState(1)
  const [revenues, setRevenues] = useState<IDataRevenue[]>([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const unsubscribe = getRevenues(setRevenues, setLoading, true)
    return () => unsubscribe()
  }, [])

  const pages = Math.ceil(revenues.length / rowsPerPage)

  const hasSearchFilter = Boolean(filterValue)

  const headerColumns = React.useMemo(() => {
    if (visibleColumns === 'all') return columnsCosts

    return columnsCosts.filter((column) =>
      Array.from(visibleColumns).includes(column.uid)
    )
  }, [visibleColumns])

  const filteredItems = React.useMemo(() => {
    if (!filterValue) return revenues // Retorna todos os blogs se o valor de filtro estiver vazio

    return revenues
  }, [filterValue, revenues])

  const items = React.useMemo(() => {
    const start = (page - 1) * rowsPerPage
    const end = start + rowsPerPage

    return filteredItems.slice(start, end)
  }, [page, filteredItems, rowsPerPage])

  const handleOpenModal = (id: string) => {
    setSelectedRevenueId(id)
    onOpenDelete()
  }

  const sortedItems = React.useMemo(() => {
    return items
  }, [sortDescriptor, items])

  const renderCell = React.useCallback(
    (revenue: IDataRevenue, columnKey: React.Key) => {
      const cellValue =
        revenue.revenue[columnKey as keyof IDataRevenue['revenue']]

      switch (columnKey) {
        case 'user':
          const user: IUser | undefined = getUserById(revenue.revenue.user)
          return (
            <User
              avatarProps={{
                radius: 'full',
                size: 'sm',
                src: user?.profile_image,
              }}
              classNames={{
                description: 'text-default-500',
              }}
              description={user?.email}
              name={user?.name}
            />
          )
        case 'category':
          const category: IRevenueCategory | undefined = getRevenueCategoryById(
            revenue.revenue.category
          )

          return <p>{category?.name}</p>
        case 'costs':
          return <p>{formatCurrency(revenue.revenue.costs)}</p>
        case 'date':
          return <p>{formatDateString(revenue.revenue.date, 'short')}</p>

        case 'actions':
          return (
            <div className="relative flex items-center gap-2">
              {/* <Tooltip content="Editar despesa">
              <button
                onClick={() => handleOpenModal(expense.id)}
                className="text-lg text-danger cursor-pointer active:opacity-50"
              >
                <IconPencil stroke={2} className="text-green-600" />
              </button>
            </Tooltip> */}
              <Tooltip color="danger" content="Deletar">
                <button
                  onClick={() => handleOpenModal(revenue.id)}
                  className="text-lg text-danger cursor-pointer active:opacity-50"
                >
                  <IconTrash stroke={2} />
                </button>
              </Tooltip>
            </div>
          )
        default:
          return cellValue
      }
    },
    []
  )

  const onRowsPerPageChange = React.useCallback(
    (e: React.ChangeEvent<HTMLSelectElement>) => {
      setRowsPerPage(Number(e.target.value))
      setPage(1)
    },
    []
  )

  const onSearchChange = React.useCallback((value?: string) => {
    if (value) {
      setFilterValue(value)
      setPage(1)
    } else {
      setFilterValue('')
    }
  }, [])

  const topContent = React.useMemo(() => {
    return (
      <>
        <header>
          <h1>Ganhos</h1>
        </header>
        <div className="flex flex-col  gap-4">
          <div className="flex justify-end gap-3 items-end">
            <div className="flex gap-3">
              <Dropdown>
                <DropdownTrigger className="hidden sm:flex">
                  <Button
                    endContent={<IconChevronDown className="text-small" />}
                    size="sm"
                    variant="flat"
                  >
                    Colunas
                  </Button>
                </DropdownTrigger>
                <DropdownMenu
                  disallowEmptySelection
                  aria-label="Table Columns"
                  closeOnSelect={false}
                  selectedKeys={visibleColumns}
                  selectionMode="multiple"
                  onSelectionChange={setVisibleColumns}
                >
                  {columnsCosts.map((column: any) => (
                    <DropdownItem key={column.uid} className="capitalize">
                      {capitalize(column.name)}
                    </DropdownItem>
                  ))}
                </DropdownMenu>
              </Dropdown>
              <Button
                className="bg-foreground text-background"
                endContent={<IconPlus />}
                size="sm"
                onPress={onOpen}
              >
                Adicionar novo ganho
              </Button>
              <CreateCostModal
                id=""
                isOpen={isOpen}
                onClose={onClose}
                placement="top-center"
              />
            </div>
          </div>
        </div>
      </>
    )
  }, [
    filterValue,
    onSearchChange,
    statusFilter,
    visibleColumns,
    onOpen,
    isOpen,
    onClose,
  ])

  return (
    <div className="w-full flex flex-col gap-8">
      {topContent}
      <Table
        aria-label="Example table with dynamic content & infinity pagination"
        sortDescriptor={sortDescriptor}
        onSortChange={setSortDescriptor}
        bottomContent={
          revenues.length > 0 && ( // Verificação condicional
            <div className="py-2 px-2 flex w-full justify-end">
              <Pagination
                isCompact
                page={page}
                size="sm"
                total={pages}
                onChange={setPage}
                classNames={{
                  cursor: 'bg-black text-white',
                }}
              />
            </div>
          )
        }
      >
        <TableHeader columns={headerColumns}>
          {(column) => (
            <TableColumn
              key={column.uid}
              allowsSorting={column.uid === 'name'}
              align={column.uid === 'actions' ? 'center' : 'start'}
            >
              {column.name}
            </TableColumn>
          )}
        </TableHeader>
        <TableBody emptyContent="Nenhum item encontrado" items={sortedItems}>
          {(item: IDataRevenue) => (
            <TableRow key={item.id}>
              {(columnKey) => (
                <TableCell>{renderCell(item, columnKey)}</TableCell>
              )}
            </TableRow>
          )}
        </TableBody>
      </Table>
      <ConfirmModal
        size="lg"
        isOpen={isOpenDelete}
        onClose={onCloseDelete}
        onConfirm={() => {
          deleteRevenue(selectedRevenueId, setLoading)
        }}
        message="Tem certeza que deseja deletar essa receita?"
        title="Excluir receita"
        confirm="Excluir"
        close="Fechar"
      />
    </div>
  )
}
