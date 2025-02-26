def Word_anton(word):
    r_index = -1
    m_index = -1
    for i, char in enumerate(word):
        if char == 'R':
            r_index = i
        elif char == 'M':
            m_index = i
    if r_index > m_index:
        return 'No'
    elif r_index < m_index:
        return 'yes'
    
print(Word_anton('MRS'))
            