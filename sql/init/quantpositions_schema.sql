-- Drop tables if they already exist
DROP TABLE IF EXISTS applied;
DROP TABLE IF EXISTS positions;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS users;

-- Create the users table
CREATE TABLE users (
    usrid VARCHAR(10) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    address_first VARCHAR(100) NOT NULL,
    address_second VARCHAR(100) NOT NULL,
    school VARCHAR(100),
    level VARCHAR(10) CHECK (level IN ('Intern', 'NewGrad', 'Associate', 'Senior', 'VP')),
    password_hash TEXT NOT NULL,
    autho VARCHAR(50) DEFAULT 'read' CHECK (autho IN ('read', 'edit', 'admin')),
    cover_letter TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the companies table
CREATE TABLE companies (
    cpid VARCHAR(50) PRIMARY KEY,
    cpname VARCHAR(255) NOT NULL,
    industry VARCHAR(50) CHECK (industry IN (
        'HedgeFund', 'QuantTrading', 'AssetManagement', 'InvestmentBank',
        'CommercialBank', 'FinancialServices', 'Insurance', 'FinancialAdvisor',
        'Fintech', 'Technology', 'Exchange', 'Consulting', 'PensionFund', 'Etc'
    )),
    importance INTEGER CHECK (importance IN (1, 2, 99)) DEFAULT 99,
    headquarter_first VARCHAR(100),
    headquarter_first VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(20)
);

-- Create the positions table
CREATE TABLE positions (
    pztid VARCHAR(50) PRIMARY KEY,
    cpid VARCHAR(50) REFERENCES companies(cpid) ON DELETE CASCADE,
    pztname VARCHAR(255) NOT NULL,
    pztlevel VARCHAR(20) CHECK (pztlevel IN ('Intern', 'NewGrad', 'Associate', 'Senior', 'VP')),
    year INTEGER NOT NULL,
    url TEXT,
    jd TEXT,
    note TEXT,
    active BOOLEAN DEFAULT TRUE,
    deadline TIMESTAMP,
    updated_by VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the applied table
CREATE TABLE applied (
    usrid VARCHAR(50) REFERENCES users(usrid) ON DELETE CASCADE,
    cpid VARCHAR(50) REFERENCES companies(cpid) ON DELETE CASCADE,
    pztid VARCHAR(50) REFERENCES positions(pztid) ON DELETE CASCADE,
    applied BOOLEAN DEFAULT FALSE,
    applied_at TIMESTAMP,
    PRIMARY KEY (usrid, pztid)
);