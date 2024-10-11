'use client'
import {
  Table,
  TableBody,
  TableCell,
  TableColumn,
  TableHeader,
  TableRow,
  User,
} from '@nextui-org/react'
import { columns, users } from 'public/constants/movement-table/data'
import React from 'react'
import { formatCurrency } from 'src/utils/currency'

const statusColorMap: Record<
  string,
  'success' | 'danger' | 'warning' | 'default' | 'primary' | 'secondary'
> = {
  active: 'success',
  paused: 'danger',
  vacation: 'warning',
}

export default function MovementTable() {
  const renderCell = React.useCallback((user, columnKey) => {
    const cellValue = user[columnKey]

    switch (columnKey) {
      case 'name':
        return (
          <User
            avatarProps={{ radius: 'lg', src: user.avatar }}
            description={user.email}
            name={cellValue}
          >
            {user.email}
          </User>
        )
      case 'financial_transactions':
        return (
          <h2
            className={`flex flex-col font-semibold ${
              user.type_transactions === 'exit'
                ? 'text-red-600'
                : 'text-green-600'
            }`}
          >
            {user.type_transactions === 'exit' ? '-' : '+'}{' '}
            {formatCurrency(user.financial_transactions)}
          </h2>
        )
      default:
        return cellValue
    }
  }, [])

  return (
    <Table aria-label="Example table with custom cells">
      <TableHeader columns={columns}>
        {(column) => (
          <TableColumn key={column.uid} align={'center'}>
            {column.name}
          </TableColumn>
        )}
      </TableHeader>
      <TableBody items={users}>
        {(item) => (
          <TableRow key={item.id}>
            {(columnKey) => (
              <TableCell>{renderCell(item, columnKey)}</TableCell>
            )}
          </TableRow>
        )}
      </TableBody>
    </Table>
  )
}
